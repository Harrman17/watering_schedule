from datetime import timedelta, datetime


class Plant:
    def __init__(self, id, name, watering_frequency):
        self.__id = id
        self.__name = name
        self.__watering_frequency = watering_frequency
        self.__schedule = []

    def create_schedule(self, next_watering_date, weeks=12):

        end_date = next_watering_date + timedelta(weeks=weeks)

        while next_watering_date < end_date:
            if next_watering_date.weekday() == 5:
                next_watering_date -= timedelta(days=1)
            elif next_watering_date.weekday() == 6:
                next_watering_date += timedelta(days=1)

            if next_watering_date.weekday() < 5:
                self.__schedule.append(next_watering_date.strftime("%d-%m-%Y"))

            next_watering_date += timedelta(days=self.__watering_frequency)
            

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_watering_frequency(self):
        return self.__watering_frequency


    def get_schedule(self):
        return self.__schedule
