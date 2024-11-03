from lib.plant import *
from datetime import datetime, timedelta
from lib.watering_schedule import *

def test_if_instantiates_with_correct_attributes():
    plant = Plant(9, "Money Plant", 6)

    assert plant.get_id() == 9
    assert plant.get_name() == "Money Plant"
    assert plant.get_watering_frequency() == 6    
    assert plant.get_schedule() == []
# update gettters




def test_if_schedule_is_calculated():
    scheduler = WateringSchedule()
    start_date = scheduler.calculate_start_date()


    plant = Plant(8, "Bamboo", 4)

    plant.create_schedule(start_date)

    assert plant.get_schedule() == ['04-11-2024', '08-11-2024', '12-11-2024', '15-11-2024', '19-11-2024', '22-11-2024', '26-11-2024', '29-11-2024', '03-12-2024', '06-12-2024', '10-12-2024', '13-12-2024', '17-12-2024', '20-12-2024', '24-12-2024', '27-12-2024', '31-12-2024', '03-01-2025', '07-01-2025', '10-01-2025', '14-01-2025', '17-01-2025', '21-01-2025', '24-01-2025']

