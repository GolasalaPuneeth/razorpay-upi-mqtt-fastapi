from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import FastAPI,Request,Depends
from contextlib import asynccontextmanager
from Routes import paymentRoute
import time

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB tables on application startup
    # await init_db()
    yield
app = FastAPI(title="Payment API",
              description="API for handling payment processing",
               version="1.0.0",
               lifespan=lifespan)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000
    response.headers["X-Response-Time"] = f"{execution_time:.2f} ms"
    return response

app.include_router(paymentRoute)

# as sample code for refference

# @app.post("/students/", response_model=Student)
# async def create_student_endpoint(
#     student: Student, db: AsyncSession = Depends(get_db)
# ):
#     return await repo.create_student(session=db, student=student)