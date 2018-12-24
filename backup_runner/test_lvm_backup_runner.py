import unittest
from datetime import datetime
from .lvm_backup_runner import LVMBackupRunner
from backup_config.default import DefaultConfig
from scheduler.sample_scheduler import SampleScheduler
from logger.default import DefaultLogger
from backup_runner.lvm_backup_runner import LVMBackupRunner

class TestLVMBackupRunner(unittest.TestCase):
    def setUp(self):
        config = DefaultConfig('/path/from', '/mnt/savedir/', 'testbk', SampleScheduler())
        self.runner = LVMBackupRunner(config, DefaultLogger())
    def test_create_snapshot(self):
        self.assertEqual(' '.join(self.runner._create_snapshot('mysnapshot')), '/sbin/lvcreate -s --size=50G --name mysnapshot /path/from')
    def test_get_snapshot_path(self):
        self.assertEqual(self.runner._get_snapshot_path('mysnap'), '/dev/cl/mysnap')
    def test_mount_snapshot(self):
        self.assertEqual(' '.join(self.runner._mount_snapshot('frompath', 'topath')), '/bin/mount -t xfs -o ro,nouuid frompath topath')
    def test_xfsdump(self):
        self.assertEqual(' '.join(self.runner._xfsdump('mymedia', 10, '/save/path', '/snap/path')), '/sbin/xfsdump -M mymedia -L backup -l 10 -u -f /save/path /snap/path -p 300')
    def test_remove_snapshot(self):
        self.assertEqual(' '.join(self.runner._remove_snapshot('snapname')), '/sbin/lvremove cl/snapname -y')
    def test_compress(self):
        self.assertEqual(' '.join(self.runner._compress('/target/path')), '/bin/pbzip2 -p3 /target/path')
    def test_mount(self):
        self.assertEqual(' '.join(self.runner._mount('/source/path', '/target/path')), '/bin/mount /source/path /target/path')
    def test_umount(self):
        self.assertEqual(' '.join(self.runner._umount('/target/path')), '/bin/umount /target/path')