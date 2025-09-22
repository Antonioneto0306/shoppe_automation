from core.auth import obter_pedidos_ready_to_ship
from core.logistics import criar_envio, baixar_etiqueta

pedidos = obter_pedidos_ready_to_ship()

for pedido in pedidos.get("orders", []):
    order_sn = pedido["ordersn"]
    
    # Gerar código de envio
    envio = criar_envio(order_sn, logistics_id=123456)
    print(f"Envio gerado para {order_sn}: {envio}")
    
    # Aqui você chamaria o endpoint para baixar a etiqueta
    # Exemplo fictício:
    etiqueta_bytes = b"%PDF-1.4..."  # bytes do PDF vindo da API
    caminho_pdf = baixar_etiqueta(order_sn, etiqueta_bytes)
    print(f"Etiqueta salva em {caminho_pdf}")
