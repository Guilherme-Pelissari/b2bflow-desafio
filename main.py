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


