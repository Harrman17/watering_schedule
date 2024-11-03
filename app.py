from flask import Flask, render_template
import json
from lib.watering_schedule import WateringSchedule
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET'])
def plants():
    scheduler = WateringSchedule()
    plants = scheduler.get_plants_and_schedule()
    today = datetime.now()  # Get today's date
    return render_template('index.html', plants=plants, today=today, timedelta=timedelta)


if __name__ == '__main__':
    app.run(debug=True)