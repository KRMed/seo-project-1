from claude_auth import get_client
from calendar_get import get_events_today

def prompt(events):
  client = get_client()

  response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{
      "role": "user",
      "content": f"Parse this dictionary of events and return a summary of the day (MUST BE LESS THAN 300 CHARACTERS): {events}"
  }]
  )

  return response.content[0].text

test = get_events_today()
print(prompt(test))