from telethon.sync import TelegramClient
from dotenv import load_dotenv
import os

# .env
load_dotenv()
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
SESSION_NAME = 'my_telegram_session'

with TelegramClient(SESSION_NAME, api_id, api_hash) as client:
    print("Código de verificação confirmado.")
    client.start()
    print("Arquivo .session criado com sucesso")
