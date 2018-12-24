import subprocess
import os
from .base_runner import BaseBackupRunner

class LVMBackupRunner():
    commands = {
        'mount': '/bin/mount',
        'umount': '/bin/umount',
        'lvcreate': '/sbin/lvcreate',
        'lvremove': '/sbin/lvremove',
        'pbzip2': '/bin/pbzip2',
        'xfsdump': '/sbin/xfsdump'
    }
    def __init__(self, config, logger, vg_name='cl', snapshot_size='50G'):
        self.config = config
        self.logger = logger
        self.vg_name = vg_name
        self.snapshot_size=snapshot_size
    def run(self, backup_time):
        name = self.config.get_backup_name()
        level_config = self.config.get_scheduler().get_level_config(backup_time)
        level = level_config.get_level()
        self.logger.log('backup {} started'.format(name))
        snapshot_name = 'snap-{}'.format(name)
        snapshot_path = self._get_snapshot_path(snapshot_name)
        snapshot_mnt_path = '/mnt/snapshot'
        self.logger.log('taking snapshot')
        self._run_command(self._create_snapshot(snapshot_name))
        self._run_command(self._mount_snapshot(snapshot_path, snapshot_mnt_path))
        save_path = self.config.get_save_path(backup_time, level)
        self.logger.log('dumping')
        self._run_command(self._xfsdump(name, level, save_path, snapshot_path))
        self._run_command(self._umount(snapshot_mnt_path))
        self._run_command(self._remove_snapshot(snapshot_name))
        self.logger.log('compressing dump file')
        self._run_command(self._compress(save_path))
        level_config.after_backup_completed(self.config)
        self.logger.log('backup {} successfully completed'.format(name))

    def _create_snapshot(self, snapshot_name):
        return [self._get_command('lvcreate'), '-s', '--size={}'.format(self.snapshot_size), '--name', snapshot_name, self.config.get_from_path()]
    def _get_snapshot_path(self, snapshot_name):
        return '/dev/{}/{}'.format(self.vg_name, snapshot_name)
    def _mount_snapshot(self, source, target):
        self._create_dir_if_not_exists(target)
        return [self._get_command('mount'), '-t', 'xfs', '-o', 'ro,nouuid', source, target]
    def _xfsdump(self, media_name, level, save_path, snap_path):
        return [self._get_command('xfsdump'), '-M', media_name, '-L', 'backup', '-l', str(level), '-u', '-f', save_path, snap_path, '-p', '300']
    def _remove_snapshot(self, snap_name):
        return [self._get_command('lvremove'), '{0}/{1}'.format(self.vg_name, snap_name), '-y']
    def _compress(self, save_path):
        return [self._get_command('pbzip2'), '-p3', save_path]
    def _mount(self, source, target):
        self._create_dir_if_not_exists(target)
        return [self._get_command('mount'), source, target]
    def _umount(self, target):
        return [self._get_command('umount'), target]
    def _create_dir_if_not_exists(self, path):
        if os.path.exists(path):
           os.makedirs(path)
    def _get_command(self, command):
        return self.__class__.commands[command]
    def _run_command(self, command_list):
        try:
            subprocess.run(command_list)
        except subprocess.CalledProcessError as e:
            self.logger.error('An error has occurred in processing the command: {}\nDetail:{}'.format(' '.join(command_list), e.args))
            raise