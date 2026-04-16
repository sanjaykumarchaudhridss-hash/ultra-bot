from pyrogram import Client, filters
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_NAME = os.getenv("OWNER_NAME")

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("ping", prefixes="."))
async def ping(client, message):
    await message.reply("🏓 Pong!")

@app.on_message(filters.command("alive", prefixes="."))
async def alive(client, message):
    await message.reply(f"✅ Bot Alive\n👑 Owner: {OWNER_NAME}")

print("Bot Started...")
app.run()
