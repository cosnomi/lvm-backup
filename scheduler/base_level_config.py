class BaseLevelConfig:
    """
    All level config class must inherit this class
    """
    def get_level_config(self, backup_time):
        pass
    def after_backup_completed(self, backup_config):
        """
        This function is run after the backup completed.
        Delete old backup files etc...
        Parameters
        ----------
        backup_config: BackupConfig
            BackupConfig instance used for this backup
        """
        pass
