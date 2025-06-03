from pyrogram import Client, filters

api_id = 123456       # তোমার API ID
api_hash = "your_api_hash_here"
session_string = "your_session_string_here"
source_chat_id = -1001234567890
destination_chat_id = -1009876543210

app = Client(
    name="forwarder",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session_string
)

@app.on_message(filters.chat(source_chat_id))
async def forward_all(client, message):
    try:
        await message.forward(destination_chat_id)
        print(f"✅ Forwarded message {message.id}")
    except Exception as e:
        print(f"❌ Failed to forward: {e}")

app.run()
