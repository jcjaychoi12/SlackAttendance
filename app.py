import os
import asyncio
import aiohttp
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

client = WebClient(token=TOKEN)

async def test_method(message):
    print(f"Message: {message.get('text', 'Message not found')}")
    print(f"Timestamp: {message.get('ts')}")

async def listen():
    async with aiohttp.ClientSession() as session:
        url = 'https://slack.com/api/conversations.history'
        params = {
            'token': TOKEN,
            'channel': 'D073EV6RB54',
            'limit': 10
        }
        
        while True:
            async with session.get(url, params=params) as response:
                res_json = await response.json()
                
                # Process messages
                for message in res_json['messages']:
                    await test_method(message)
                
                # Check if there are more pages to fetch
                if 'has_more' in res_json and res_json['has_more']:
                    # Update the 'cursor' parameter for the next page
                    params['cursor'] = res_json['response_metadata']['next_cursor']
                else:
                    break

if __name__ == "__main__":
    asyncio.run(listen())