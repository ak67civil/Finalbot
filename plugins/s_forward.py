from pyrogram import Client, filters

@Client.on_message(filters.video & filters.private)
async def forward(client, message):
    # Optional backup forward logic
    pass
  
