import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("TRELLO_API_KEY")
api_token = os.getenv("TRELLO_API_TOKEN")
board_id = os.getenv("TRELLO_BOARD_ID")
list_id = os.getenv("TRELLO_LIST_ID")

def criar_cartao(dados):
    url = "https://api.trello.com/1/cards"

    headers = {
    "Accept": "application/json"
    }

    query = {
    'idList': {list_id},
    'key': {api_key},
    'token': {api_token},
    'name': dados["nome"],
    'desc': dados["descricao"]
    }

    response = requests.request(
    "POST",
    url,
    headers=headers,
    params=query
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))