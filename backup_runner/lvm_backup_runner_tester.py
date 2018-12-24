from .lvm_backup_runner import LVMBackupRunner

class LVMBackupRunnerTester(LVMBackupRunner):
    def _create_dir_if_not_exists(self, path):
        pass
    def _run_command(self, command_list):
        print('EXEC: {}'.format(command_list))
