from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
def get_claude_key():
  return Anthropic()