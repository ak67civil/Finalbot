from pyrogram import Client, filters
import os, sys

@Client.on_message(filters.command("start") & filters.private)
async def Start_msg(client, message):
    if len(message.text.split()) > 1:
        data = message.text.split()[1]
        if data.startswith("vid_"):
            try:
                _, priv_id, msg_id = data.split("_")
                await client.copy_message(
                    chat_id=message.chat.id,
                    from_chat_id=int(priv_id),
                    message_id=int(msg_id),
                    protect_content=True
                )
                return
            except: pass
    await message.reply_text("🛡️ **AceBot Started!**\nUse `/connect` to link channels.")

@Client.on_message(filters.command("help"))
async def help_msg(client, message):
    await message.reply_text("📖 **Help:** Admin me in channels & use `/connect`.")

@Client.on_message(filters.command("restart"))
async def restart_handler(client, message):
    await message.reply_text("🔄 Restarting...")
    os.execl(sys.executable, sys.executable, *sys.argv)

@Client.on_message(filters.command("log"))
async def log_msg(client, message):
    await message.reply_text("📊 Logs are being updated...")
  
