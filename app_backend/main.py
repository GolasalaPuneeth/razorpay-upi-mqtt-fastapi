from fastapi import FastAPI,Request
from pydantic import BaseModel
from Routes import paymentRoute
import time


app = FastAPI(title="Payment API", description="API for handling payment processing", version="1.0.0")

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000
    response.headers["X-Response-Time"] = f"{execution_time:.2f} ms"
    return response

app.include_router(paymentRoute)