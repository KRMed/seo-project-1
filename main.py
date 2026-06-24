from calendar_get import get_events_today
from claude import prompt

print("Initializing AI Assistant...")
print("Checking if you are authorized...")
events = get_events_today()
tone = input("Please the tone you would like for your assistant today: ")
print(prompt(events, tone))



