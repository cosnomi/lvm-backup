from .backup_config.default import DefaultConfig
from .scheduler.sample_scheduler import SampleScheduler
from .logger.default import DefaultLogger
from .pushover.logger import PushoverNotification
from .backup_runner.lvm_backup_runner import LVMBackupRunner
from .backup_runner.lvm_backup_runner_tester import LVMBackupRunnerTester
from datetime import datetime

scheduler = SampleScheduler()

logger = DefaultLogger([PushoverNotification('root')])
config = DefaultConfig('/dev/mapper/cl-root', '/mnt/backup1/', 'root', SampleScheduler())
runner = LVMBackupRunnerTester(config, logger, 'cl')
runner.run(datetime.now())
