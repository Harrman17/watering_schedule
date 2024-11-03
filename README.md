## Plant Watering Schedule
This is an application that takes in JSON data for plants. Using each plant's watering frequency a schedule is generated which excludes weekends (as we consider those as days off for the gardener!).
Allowing the viewer to easily see which plants need to be watered on each day of the week.

Requirements:
• The schedule should cover the next 12 weeks, starting from next Monday.
• Plants should not be watered on Saturdays or Sundays (work-life balance!).
• Each plant has a watering frequency, and the application should generate a
schedule based on that.
• Every plant should be watered on the first day of the schedule (next Monday),
after which its specific schedule should be followed as closely as possible.
• You’ve been provided with a JSON file containing data about the plants,
including their watering frequency (in days).

Acceptance Criteria:
• The user can easily view which plants to water on which date(s).
• The schedule starts on next Monday and covers the following 12 weeks.
• No watering takes place on weekends (Saturdays and Sundays).
• Each plant is watered based on its desired schedule, considering weekends.
