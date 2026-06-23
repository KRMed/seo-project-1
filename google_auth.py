from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
from dotenv import load_dotenv
import os

load_dotenv() #loads .env

scopes = ["https://www.googleapis.com/auth/calendar.readonly"]

credentials_file = os.getenv("GOOGLE_CREDENTIALS")
token_file = os.getenv("GOOGLE_TOKEN")

def get_credentials():
  creds = None
  if os.path.exists(token_file): #if token.json exist already
    creds = Credentials.from_authorized_user_file(token_file, scopes)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = Flow.from_client_secrets_file(credentials_file, scopes = scopes, redirect_uri = "urn:ietf:wg:oauth:2.0:oob")
      auth_url, _ = flow.authorization_url(prompt = "consent")
      print("Paste this in a new browser tab: ", auth_url)
      code = input("Paste the code you received here: ")
      flow.fetch_token(code = code)
      creds = flow.credentials
    with open(token_file, "w") as token:
      token.write(creds.to_json())
  return creds

# if __name__ == "__main__":            #test to see if connection works
#   creds = get_credentials()
#   print("Success: ", creds.valid)