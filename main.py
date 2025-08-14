#imports necessários
import os
import requests
from supabase import create_client
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Lê as variáveis de ambiente necessárias para conexão com Supabase e Z-API
# Olhar no README o passo a passo de como obter as variáveis de ambiente e configurar o .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

# Conectar no Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def buscar_contatos():
    """
    Busca até 3 registros da tabela 'contatos' no Supabase.
    Retorna uma lista de dicionários com os dados dos contatos.
    Em caso de erro, retorna lista vazia.
    """
    try:
        response = supabase.table("contatos").select("*").limit(3).execute()
        return response.data
    except Exception as e:
        print(f"Erro ao buscar contatos: {e}")
        return []
    
def enviar_mensagem(numero, nome):
    """
    Envia mensagem personalizada para um número via API da Z-API.
    
    Parâmetros:
        numero (str): Número de telefone no formato internacional (ex: 5511999999999)
        nome (str): Nome da pessoa para personalizar a mensagem
    """

    # URL da API para envio de mensagens de texto
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"

    # Dados enviados no corpo da requisição
    payload = {
        "phone": numero,
        "message": f"Olá {nome}, tudo bem com você?"
    }
    
    # Cabeçalho da requisição com CLIENT_TOKEN (ler README para saber como obter o token)
    headers = {
        "Content-Type": "application/json",
        "Client-Token": ZAPI_CLIENT_TOKEN  
    }

    # Envia a requisição HTTP POST
    try:
        r = requests.post(url, json=payload, headers=headers)
        print(f"Mensagem enviada para {nome} ({numero}): {r.status_code}")
        print("Resposta:", r.text)
    except Exception as e:
        print(f"Erro ao enviar mensagem para {nome}: {e}")

# Bloco de execução
if __name__ == "__main__":
    contatos = buscar_contatos()
    if not contatos:
        print("Nenhum contato encontrado.")
    else:
        for contato in contatos:
            enviar_mensagem(contato["telefone"], contato["nome"])

