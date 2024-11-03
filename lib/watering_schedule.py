from datetime import datetime, timedelta
from lib.plant import Plant
import json


    # next monday function
class WateringSchedule():
    def __init__(self):
        pass

    def get_plants_and_schedule(self):
        plants_json = self.read_json()
        start_date = self.calculate_start_date() # returns the next monday and assigned due to sunday issue
        plants = []

        for plant in plants_json:
            new_plant = Plant(plant['plant_id'], plant['name'], plant['watering_frequency'])
            new_plant.create_schedule(start_date)
            plants.append(new_plant)

        return plants
    
    def calculate_start_date(self):
        today = datetime.now()
        days_till_next_monday = (7 - today.weekday()) % 7
        next_monday = today + timedelta(days=days_till_next_monday)

        return next_monday

    def read_json(self):
        with open('lib/plants.json', 'r') as file:
            plants = json.load(file)
        return plants
