import requests
import base64
import os

def withdraw(amount):
    client_id = os.getenv("PAYPAL_CLIENT_ID")
    secret = os.getenv("PAYPAL_SECRET")
    cred = base64.b64encode(f"{client_id}:{secret}".encode()).decode()
    headers = {
        "Authorization": f"Basic {cred}",
        "Content-Type": "application/json"
    }
    data = {
        "sender_batch_header": {"sender_batch_id": f"payout_{int(time.time())}"},
        "items": [{
            "recipient_type": "EMAIL",
            "amount": {"value": f"{amount:.2f}", "currency": "USD"},
            "receiver": os.getenv("PAYPAL_EMAIL")
        }]
    }
    res = requests.post("https://api-m.paypal.com/v1/payments/payouts", json=data, headers=headers)
    print("인출 결과:", res.json())
