import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": "🔥 *MEME RADAR AI* est en ligne. Test via GitHub Actions réussi !",
    "parse_mode": "Markdown",
}

print("Envoi en cours...")
r = requests.post(url, json=payload, timeout=10)

if r.status_code == 200 and r.json().get("ok"):
    print("✅ Message envoyé avec succès sur Telegram !")
else:
    print("❌ Échec :", r.status_code, r.text)
    raise SystemExit(1)
