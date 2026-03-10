import requests
import datetime


# --- VERIFICACIÓN DE FECHA ---
hoy = datetime.datetime.now()
# --- CONFIGURACIÓN DE GREEN-API ---
ID_INSTANCE = "7103541592"
API_TOKEN = "f6523539fd1041a8a4bcc11768ff302b3d362f9a4f834baebb"
# El número debe ir con código de país, ejemplo: 51999888777 (sin el +)
GROUP_ID = "51958314428-1586272632@g.us" 

url = f"https://api.green-api.com/waInstance{ID_INSTANCE}/sendMessage/{API_TOKEN}"

payload = {
    "chatId": GROUP_ID,
    "message": """¡Buenos días! 
    Pasamos por aquí para recordarles que hoy es día 9, fecha programada para el pago del mantenimiento mensual. ✨ 
    ¿Cómo cumplir con el pago? 
      1️⃣ Realiza tu depósito por yape o plin.
      2️⃣ Envía la foto de tu comprobante por aquí
      ⚠️ Nota importante: Recuerden que realizarlo hoy nos ayuda a todos a evitar el recargo por mora. ¡Agradecemos mucho su puntualidad!
      
      ¡Que tengan un excelente día!"""
}

headers = {
    'Content-Type': 'application/json'
}

# --- ENVÍO ---
try:
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("¡Mensaje enviado con éxito!")
    else:
        print(f"Error al enviar: {response.text}")
except Exception as e:
    print(f"Ocurrió un error: {e}")