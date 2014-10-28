from TimeUnitEnum import TimeUnitEnum
import datetime

class MyDateUtil:
    @staticmethod
    def get_first_and_last_day(date, unit):
        if(unit == TimeUnitEnum.day.value):
            return (date, date+datetime.timedelta(days=1))
        elif(unit == TimeUnitEnum.week.value):
            first_day = date - datetime.timedelta(days=(date.weekday()+1)%7)
            last_day = first_day + datetime.timedelta(days=6)
            return (first_day, last_day)
