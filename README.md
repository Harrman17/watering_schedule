## Plant Watering Schedule
This is an application that takes in JSON data for plants. Using each plant's watering frequency a schedule is generated which excludes weekends (as we consider those as days off for the gardener!).
Allowing the viewer to easily see which plants need to be watered on each day of the week.

### Requirements:
• The schedule should cover the next 12 weeks, starting from next Monday.  
• Plants should not be watered on Saturdays or Sundays (work-life balance!).  
• Each plant has a watering frequency, and the application should generate a
schedule based on that.  
• Every plant should be watered on the first day of the schedule (next Monday),
after which its specific schedule should be followed as closely as possible.  
• You’ve been provided with a JSON file containing data about the plants,
including their watering frequency (in days).  

### Acceptance Criteria:
• The user can easily view which plants to water on which date(s).  
• The schedule starts on next Monday and covers the following 12 weeks.  
• No watering takes place on weekends (Saturdays and Sundays).  
• Each plant is watered based on its desired schedule, considering weekends.  

## Flowchart:
![flowchart](https://github.com/Harrman17/watering_schedule/blob/63c6add72e599427c3032fbca0704d74ed6c52fe/Watering%20Schedule.pdf)

## How to run:
#### Once the project is cloned to your device please install the dependencies using by running the below in your teminal  
1. pip install -r requirements.txt

#### run the app  
2. python app.py  

click on the local host link to view it
