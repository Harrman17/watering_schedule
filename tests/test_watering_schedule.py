from lib.watering_schedule import *
from datetime import datetime, timedelta


def test_if_start_date_calculated():
    scheduler = WateringSchedule()
    today = datetime.now()
    days_till_next_monday =  (7 - today.weekday()) % 7 
    date = today + timedelta(days=days_till_next_monday)
    expected_date = date.weekday()

    assert scheduler.calculate_start_date().weekday() == expected_date


