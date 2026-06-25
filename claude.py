from claude_auth import get_client
from calendar_get import get_events_today
from db import save_log, get_logs
from datetime import date

def prompt(events, tone):
  client = get_client()

  response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{
      "role": "user",
      "content": f"""
        You are a personal calendar assitant. You will be given a list of the days calendar events
        Your job is to:
        - Identify the events that are high priority (ex. deadlines, short prep windows, or multiple attendants) and whats low priority
        - Flag any conflicts, scheduling issues, or gaps that aren't realistic
        - Suggest things to prepare before key events
        - If there are free blocks, suggest maybe ways to use them
        - If the day is a light day then say that, otherwise if it's jampacked take into consideration burnout and faitgue

        Tone to follow: {tone}
        Keep your response under 200 words, no bullet points longer than a sentence

        Formatting rules:
        - No markdown, no bold or italics, no headers or horizontal rules
        - Keep it to plain text only. Write like you're texting someone or having a normal conversation with a rundown of their day
        - Use line breaks only to separate ideas, not as symbols or decorators
        - Keep it nice, aesthetic, and easy to read

        Do not just reguritate the calendar back to the user, provide real value as an assitant with analysis and advice

        Today's events:
        {events}
      """
    }]
  )

  return response.content[0].text

# #Testing
# test = get_events_today()
# tone = "Cheerful"
# summary = prompt(test, tone)
# print(summary)

# save_log(str(date.today()), summary)

# for log in get_logs():
#   print(f"{log.date} - {log.summary}")