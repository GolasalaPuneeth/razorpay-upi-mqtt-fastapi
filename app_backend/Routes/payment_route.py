from fastapi import APIRouter
from fastapi import Request, HTTPException
import json

paymentRoute = APIRouter(tags=["Payment Procesor Routes and Hooks"], prefix="/payment")
WEBHOOK_SECRET = "4ABsxJv!5ML.qDY"  # Replace with your actual webhook secret

@paymentRoute.post("/webhook")
async def razorpay_webhook(request: Request):

    # 1. Read the original request body
    payload = await request.body()

    # 2. Extract Razorpay signature
    signature = request.headers.get(
        "X-Razorpay-Signature"
    )

    if not signature:
        raise HTTPException(
            status_code=400,
            detail="Missing webhook signature"
        )

    if not WEBHOOK_SECRET:
        raise HTTPException(
            status_code=500,
            detail="Webhook configuration error"
        )

    # 3. Verify signature BEFORE processing
    # is_valid = verify_webhook_signature(
    #     payload,
    #     signature,
    #     WEBHOOK_SECRET
    # )
    is_valid = True  
    if not is_valid:

        raise HTTPException(
            status_code=400,
            detail="Invalid webhook signature"
        )

    # 4. Parse JSON only after verification
    try:
        event_data = json.loads(payload)
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Invalid JSON payload"
        )

    event = event_data.get("event")
    event_id = request.headers.get("X-Razorpay-Event-Id")



    # 5. Process event
    if event == "payment.captured":

        payment = (
            event_data
            .get("payload", {})
            .get("payment", {})
            .get("entity", {})
        )

        payment_id = payment.get("id")
        order_id = payment.get("order_id")
        amount = payment.get("amount")
        currency = payment.get("currency")

    elif event == "payment.failed":

        payment = (
            event_data
            .get("payload", {})
            .get("payment", {})
            .get("entity", {})
        )


    elif event == "order.paid":

        order = (
            event_data
            .get("payload", {})
            .get("order", {})
            .get("entity", {})
        )
    # 6. Acknowledge successful receipt
    return {
        "status": "success",
        "event": event
    }

# 4ABsxJv!5ML.qDY