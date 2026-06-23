from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from dotenv import load_dotenv
import os

load_dotenv() #loads .env

scopes = ["https://www.googleapis.com/auth/calendar.readonly"]

credentials_file = os.getenv("GOOGLE_CREDENTIALS")
token_file = os.getenv("GOOGLE_TOKEN")

def get_credentials():
  creds = None
  if os.path.exists(token_file):
    creds = Credentials.from_authorized_user_file(token_file, scopes)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(credentials_file, scopes)
      creds = flow.run_console()
    with open(token_file, "w") as token:
      token.write(creds.to_json())
  return creds