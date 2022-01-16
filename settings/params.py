from enum import Enum

# Ratio for time sleeps
time_reducer_factor = 1

# Number of foobar to build in one cycle
foobar_to_build_in_one_cycle = 3

# Number of bot to reach to stop the process
max_bot = 30

class Workshops(Enum):
    FOO_MINE = 1
    BAR_MINE = 2 
    ASSEMBLY_LINE = 3
    FOOBAR_MARKET_PLACE = 4
    ROBOT_MARKET_PLACE = 5



