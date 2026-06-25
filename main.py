from calendar_get import get_events_today
from claude import prompt
from db import save_log, get_logs, get_log_by_date
from datetime import date

print("Initializing AI Assistant...")
print("Checking if you are authorized...")
events = get_events_today()
print("Authorization Successful \n")

def menu():
  while True:
    print("1. Create today's summary")
    print("2. View past summaries")
    print("3. View summary by date")
    print("4. Exit")

    choice = str(input("\nPick an option:").strip())

    if choice == "1":
      tone = input("Please enter the tone you would like for your assistant today: ")
      summary = prompt(events, tone)
      print(f"\n{summary}")
      today = str(date.today())
      save_log(today, summary)
      print(f"\nLog saved for {today}")
    
    elif choice == "2":
      logs = get_logs()
      if not logs: #if logs haven't been created yet
        print("\nNo logs created yet")
      for log in logs:
        print(f"\nDate: {log.date}")
        print(log.summary)
    
    elif choice == "3":
      day = input("Enter date (YYYY-MM-DD): ").strip()
      log = get_log_by_date(day)
      if log:
        print(f"\nDate:{log.date}")
        print(log.summary)
      else:
        print("\nNo logs for that date")
    
    elif choice == "4":
      print("Have a good day!")
      break
    
    else:
      print("Invalid Option")

if __name__ == "__main__":
  menu()