from telethon import TelegramClient
from dotenv import load_dotenv
import sys
import os
import asyncio


# .env
load_dotenv()
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
SESSION_NAME = 'my_telegram_session'

destinatario = sys.argv[1] # Destinatário
mensagem = sys.argv[2]  # Mensagem

async def enviarMensagem():
    async with TelegramClient(SESSION_NAME, api_id, api_hash) as client:
        try:
            await client.send_message(destinatario, mensagem)
            # print(f"✔ Mensagem enviada para {destinatario}")
        except Exception as e:
            e
            
# Export fx
asyncio.run(enviarMensagem())