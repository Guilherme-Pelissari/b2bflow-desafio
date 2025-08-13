import os
import requests
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def buscar_contatos():
    try:
        response = supabase.table("contatos").select("*").limit(3).execute()
        return response.data
    except Exception as e:
        print(f"Erro ao buscar contatos: {e}")
        return []
    
def enviar_mensagem(numero, nome):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"
    payload = {
        "phone": numero,
        "message": f"Olá {nome}, tudo bem com você?"
    }
    headers = {
        "Content-Type": "application/json",
        "Client-Token": ZAPI_CLIENT_TOKEN  
    }
    try:
        r = requests.post(url, json=payload, headers=headers)
        print(f"Mensagem enviada para {nome} ({numero}): {r.status_code}")
        print("Resposta:", r.text)
    except Exception as e:
        print(f"Erro ao enviar mensagem para {nome}: {e}")


if __name__ == "__main__":
    contatos = buscar_contatos()
    if not contatos:
        print("Nenhum contato encontrado.")
    else:
        for contato in contatos:
            enviar_mensagem(contato["telefone"], contato["nome"])

