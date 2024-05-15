import os
import asyncio
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

client = WebClient(token=TOKEN)

async def test_method(event):
    print(f"Message: {event.get("text", "Message not found")}")
    print(f"Timestamp: {event.get("ts")}")