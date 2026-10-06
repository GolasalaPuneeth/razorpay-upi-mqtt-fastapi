from fastapi import APIRouter,Header,Depends
from fastapi import Request, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
import json
import hmac
import hashlib
from Database_Layer import get_db
from Service_Layer import IPaymentHook,PaymentHook
from dotenv import load_dotenv
import os
load_dotenv()
paymentRoute = APIRouter(tags=["Payment Procesor Routes and Hooks"], prefix="/payment")
WEBHOOK_SECRET = os.getenv('RAZORPAY_WEBHOOK_SECRET')
services: IPaymentHook = PaymentHook()

@paymentRoute.post("/webhook")
async def razorpay_webhook(
    request: Request,
    x_razorpay_signature: str = Header(None),
    x_razorpay_event_id: str = Header(None),
    session:AsyncSession= Depends(get_db)
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
        # print(data)
        # Amount = payload['payload']['payment']['entity']['amount']
        # Qr_ID = payload['payload']['qr_code']['entity']['id']
        # print(Amount,Qr_ID)
        await services.process_payment(data,session)
    return {"status": "ok"}

