from .level_config.level0 import Level0Config
from .level_config.level1 import Level1Config
from .level_config.level2 import Level2Config
from .level_config.level3 import Level3Config
from .level_config.level4 import Level4Config

class SampleScheduler:
    def get_level_config(self, backup_time):
        weekday = backup_time.weekday()
        month = backup_time.month
        day = backup_time.day
        if weekday != 2:
            return Level4Config()
        elif day > 7:
            return Level3Config()
        elif month in [1, 7]:
            return Level0Config()
        elif month in [3, 5, 9, 11]:
            return Level1Config()
        else:
            return Level2Config()
