from googleapiclient.discovery import build
from datetime import datetime, timezone
from google_auth import get_credentials

def get_events_today():
  creds = get_credentials()
  connection = build("calendar", "v3", credentials = creds)

  today = datetime.now(timezone.utc)
  day_start = today.replace(hour = 0, minute = 0, second = 0, microsecond = 0).isoformat()
  day_end = today.replace(hour = 23, minute = 59, second = 59, microsecond = 0).isoformat()

    
  calendars = connection.calendarList().list().execute().get("items", [])

  all_events = []
    
  for calendar in calendars:
    cal_id = calendar["id"]
    result = connection.events().list(calendarId = cal_id, timeMin = day_start, timeMax = day_end, singleEvents = True, orderBy = "startTime").execute()

    all_events.extend(result.get("items", []))
  
  return all_events

