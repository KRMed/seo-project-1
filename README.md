# Google Calendar Personal AI Assistant

## General Information

This CLI based project connects to your Google Calendar via
OAuth 2.0 and uses Claude AI to summarize the fetched 
events for the current day. The reponse is formatted into 
a digestible chunk. Each interaction is logged to a local SQLite database for record keeping and the tone of the 
AI is customizable. 

## Requirements 
Please refer to requirements.txt

## Stack
- Python
- Google Calendar API
- Claude API
- SQLite/SQLAlchemy/Pandas

## Usage
1. Run main.py
2. If you are not authorized, the program will provide 
instructions in the terminal for OAuth.
3. Once your token.json has been created, a menu will appear.
4. Select the corresponding menu options and follow the 
instructions provided in the terminal.
