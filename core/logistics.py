import time
import hmac
import hashlib
import requests
import json
import os
from datetime import datetime
from utils.config import PARTNER_ID, PARTNER_KEY, ACCESS_TOKEN, SHOP_ID

BASE_URL = "https://partner.shopeemobile.com"

def gerar_assinatura(path, timestamp, body=""):
    base_string = f"{PARTNER_ID}{path}{timestamp}{body}"
    return hmac.new(PARTNER_KEY.encode(), base_string.encode(), hashlib.sha256).hexdigest()

def criar_envio(order_sn, logistics_id, tracking_no=""):
    path = "/api/v2/logistics/ship_order"
    timestamp = int(time.time())
    body = {
        "ordersn": order_sn,
        "shop_id": SHOP_ID,
        "logistics_id": logistics_id,
        "tracking_no": tracking_no
    }
    sign = gerar_assinatura(path, timestamp, json.dumps(body))
    params = {
        "partner_id": PARTNER_ID,
        "timestamp": timestamp,
        "sign": sign,
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(BASE_URL + path, params=params, json=body)
    return response.json()




def baixar_etiqueta(order_sn, etiqueta_bytes):
    base_path = "data/etiquetas"
    subfolder = datetime.now().strftime("%Y-%m-%d")
    save_path = os.path.join(base_path, subfolder)
    os.makedirs(save_path, exist_ok=True)
    
    pdf_filename = os.path.join(save_path, f"etiqueta_{order_sn}.pdf")
    with open(pdf_filename, "wb") as f:
        f.write(etiqueta_bytes)
    return pdf_filename
