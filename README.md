# Shopee Automation

Automação para vendedores da Shopee: busca pedidos prontos para envio, gera códigos de envio (AWB), baixa etiquetas em PDF e organiza para impressão. Ideal para agilizar a logística de lojas e servir como projeto de portfólio.

---

## 🛠 Tecnologias
- Python 3.x  
- Requests  
- Flask (opcional, para painel web)  
- python-dotenv  

---

## 🚀 Funcionalidades
- Autenticação na API da Shopee  
- Listagem de pedidos `READY_TO_SHIP`  
- Geração automática de códigos de envio (AWB)  
- Download e organização de etiquetas em PDF  
- Impressão automática das etiquetas  
- (Opcional) Painel web com Flask para visualização e controle  

---

## ⚙️ Pré-requisitos
- Conta de vendedor na Shopee  
- App criado na Shopee Open Platform  
- `partner_id`, `partner_key`, `shop_id` e `access_token`  

---

## 💻 Instalação
1. Clone o repositório:
```bash
git clone https://github.com/seu_usuario/shopee_automation.git
cd shopee_automation
