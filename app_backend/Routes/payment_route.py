from fastapi import APIRouter,Header
from fastapi import Request, HTTPException
import json
import hmac
import hashlib

paymentRoute = APIRouter(tags=["Payment Procesor Routes and Hooks"], prefix="/payment")
WEBHOOK_SECRET = ""  # Replace with your actual webhook secret

@paymentRoute.post("/webhook")
async def razorpay_webhook(
    request: Request,
    x_razorpay_signature: str = Header(None),
    x_razorpay_event_id: str = Header(None)
    ):
    # 1. Read raw body
    body = await request.body()

    # 2. Verify signature
    generated_signature = hmac.new(
        WEBHOOK_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(generated_signature, x_razorpay_signature):
        raise HTTPException(status_code=400, detail="Invalid signature")

    # 3. Parse JSON
    payload = json.loads(body)
    event = payload.get("event")

    print("Event:", event)

    # 4. Handle events
    if event == "qr_code.credited":
        data = payload["payload"]["qr_code"]["entity"]

        # payment_id = data.get("payment_id")
        # amount = data.get("amount")

        # print("Payment received:", payment_id, amount)
        # print(payload)
        print(data)
        Amount = payload['payload']['payment']['entity']['amount']
        Qr_ID = payload['payload']['qr_code']['entity']['id']
        # await Services.push_service(qrid=Qr_ID,amount=Amount,vpa="saple@123")
        print(Amount,Qr_ID)
    return {"status": "ok"}

