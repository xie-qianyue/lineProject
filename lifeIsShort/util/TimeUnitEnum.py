from enum import Enum

class TimeUnitEnum(Enum):
    """
    Enum of time unit on day
    """
    day = 1
    week = 7
    month = 30
    year = 365

    @staticmethod
    def get_time_unit_name(value):
        '''
        return a string : this day, this month, etc
        '''
        for unit in TimeUnitEnum:
            if(unit.value == value):
                return unit.name    

    @staticmethod
    def get_this_time_unit_name(value):
        '''
        return a string : this day, this month, etc
        '''
        for unit in TimeUnitEnum:
            if(unit.value == value):
                return 'this '+unit.name
