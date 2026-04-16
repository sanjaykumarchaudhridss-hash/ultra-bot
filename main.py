from pyrogram import Client, filters
import os

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_NAME = os.getenv("OWNER_NAME")

if not API_ID or not API_HASH or not BOT_TOKEN:
    print("❌ Missing Variables!")
    exit()

app = Client("bot", api_id=int(API_ID), api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("ping", prefixes="."))
async def ping(client, message):
    await message.reply("🏓 Pong!")

@app.on_message(filters.command("alive", prefixes="."))
async def alive(client, message):
    await message.reply(f"✅ Alive\nOwner: {OWNER_NAME}")

print("Bot Started Successfully 🔥")
app.run()
