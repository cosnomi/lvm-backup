from .base_backup_config import BaseBackupConfig
from datetime import datetime
from os import path
class DefaultConfig(BaseBackupConfig):
    DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'
    def __init__(self, from_path, save_dir, backup_name, scheduler):
        """
        Init this config
        Parameters
        ----------
        from_path: string
            The path of the target of the backup
        save_dir: string
            The path of the directory to save the backup file
        backup_name: string
            A short unique name that is used in dump file name or logging
        scheduler: Scheduler
        """
        self.from_path = from_path
        self.save_dir = save_dir
        self.backup_name = backup_name
        self.scheduler = scheduler
    def get_from_path(self):
        return self.from_path
    def get_save_path(self, backup_time, level):
        return path.join(self.save_dir, '{}_level{}_{}'.format(backup_time.strftime(self.DATE_FORMAT), level, self.backup_name))
    def get_backup_name(self):
        return self.backup_name
    def get_scheduler(self):
        return self.scheduler
