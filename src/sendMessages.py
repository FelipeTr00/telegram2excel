import pandas as pd
from telethon import TelegramClient
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
SESSION_NAME = "my_telegram_session"
EXCEL_FILE = "Mensagens.xlsx"

async def enviarMensagem(destinatario: str, nome: str, mensagem: str):

    async with TelegramClient(SESSION_NAME, api_id, api_hash) as client:
        try:
            await client.send_message(destinatario, mensagem)
            print(f"[SUCESSO] Mensagem enviada para {nome} → {destinatario} → {mensagem}")
        except Exception as e:
            print(f"[ERRO] Falha ao enviar a mensagem para {destinatario}: {e}")



async def main():

    try:
        df = pd.read_excel(EXCEL_FILE)

        colunas_esperadas = ["NÚMERO", "NOME", "MENSAGEM"]
        if not all(coluna in df.columns for coluna in colunas_esperadas):
            print("[ERRO] O arquivo Excel não contém as colunas esperadas.")
            return

        for index, row in df.iterrows():
            destinatario = str(row["NÚMERO"]).strip()
            nome = str(row["NOME"]).strip()
            mensagem = str(row["MENSAGEM"]).strip()

            if destinatario and mensagem:
                await enviarMensagem(destinatario, nome, mensagem)
            else:
                print(f"[ALERTA] Linha {index + 1} ignorada: Número ou mensagem vazia.")

    except Exception as e:
        print(f"[ERRO] ao processar o arquivo Excel: {e}")

# EXPORT
if __name__ == "__main__":
    asyncio.run(main())
