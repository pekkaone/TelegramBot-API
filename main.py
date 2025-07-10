from fastapi import FastAPI
from bot import run_bot
from contextlib import asynccontextmanager
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(run_bot())
    yield

app = FastAPI(lifespan=lifespan)

@app.get('/')
async def root():
    return {"bot": "running"}
