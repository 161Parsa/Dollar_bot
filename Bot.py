import requests
from datetime import datetime
import os

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = "https://api.exchangerate-api.com/v4/latest/USD"
data = requests.get(url).json()

eur = data["rates"]["EUR"]
gbp = data["rates"]["GBP"]
jpy = data["rates"]["JPY"]

now = datetime.now()
tarikh = now.strftime("%Y-%m-%d")
saat = now.strftime("%H:%M:%S")

matn = f"""Gheymat Arz ({tarikh} - {saat})

1 USD = {eur} EUR
1 USD = {gbp} GBP
1 USD = {jpy} JPY"""

send_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
response = requests.post(send_url, data={"chat_id": CHAT_ID, "text": matn})
print("Status:", response.status_code)
print("Payam ersal shod!")
