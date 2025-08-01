from fastapi import FastAPI
from bot import run_bot
from contextlib import asynccontextmanager
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(run_bot())
    yield

app = FastAPI(lifespan=lifespan)

@app.get('/', include_in_schema=False)
async def root():
    return {"bot": "running"}

@app.head('/')
async def rootb():
    return {"bot": "running"}