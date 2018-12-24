class BaseBackupConfig:
    def get_from_path(self):
        pass
    def get_save_path(self, backup_time, level):
        pass
    def get_backup_name(self):
        pass
    def get_scheduler(self):
        pass
