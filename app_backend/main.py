from fastapi import FastAPI,Request
from pydantic import BaseModel
import time


app = FastAPI(title="My Application")

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000
    response.headers["X-Response-Time"] = f"{execution_time:.2f} ms"
    return response


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")
async def root():
    return {"message": "FastAPI is running123"}

@app.post('/items/')
async def items(item:Item):
    # print(item)
    return item.model_dump()