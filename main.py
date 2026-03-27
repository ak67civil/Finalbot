import os
import asyncio
from pyrogram import Client, filters

# Configs from Heroku
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Logs ke hisaab se AceBot configuration
app = Client(
    "AceBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins"),
    in_memory=True
)

async def main():
    async with app:
        # Same start message as your logs
        print("<--- @New_auto_forwardbot Started (c) PIKU --->")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
  
