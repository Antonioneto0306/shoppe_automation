import time
import requests
from utils.config import PARTNER_ID, ACCESS_TOKEN, SHOP_ID
import gerar_assinatura

BASE_URL = "https://partner.shopeemobile.com"



def obter_pedidos_ready_to_ship(page_size=10):
    path = "/api/v2/order/get_order_list"
    timestamp = int(time.time())
    params = {
        "partner_id": PARTNER_ID,
        "timestamp": timestamp,
        "access_token": ACCESS_TOKEN,
        "shop_id": SHOP_ID,
        "sign": gerar_assinatura(path, timestamp),
        "order_status": "READY_TO_SHIP",
        "page_size": page_size
    }
    response = requests.get(BASE_URL + path, params=params)
    return response.json()
