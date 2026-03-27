from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

db = {} # Simple memory storage

@Client.on_message(filters.command("connect"))
async def connect_handler(client, message):
    try:
        priv_id, pub_id = message.command[1], message.command[2]
        db[priv_id] = pub_id
        await message.reply_text(f"✅ Connected: `{priv_id}` 🔄 `{pub_id}`")
    except:
        await message.reply_text("❌ `/connect -100PrivateID -100PublicID`")

@Client.on_message(filters.chat(list(db.keys())) & (filters.video | filters.document))
async def forward(client, message):
    pub_id = db.get(str(message.chat.id))
    if not pub_id: return
    
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("▶️ Watch Video", url=f"https://t.me/{client.me.username}?start=vid_{message.chat.id}_{message.id}")
    ]])
    await client.send_message(pub_id, f"📥 **{message.caption or 'New Content'}**", reply_markup=btn)

@Client.on_callback_query()
async def callback_query_handler(client, callback_query):
    await callback_query.answer("Processing...", show_alert=True)
  
