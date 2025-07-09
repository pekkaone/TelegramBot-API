from fastapi import FastAPI
from bot import run_bot
import asyncio

app = FastAPI()

@app.get('/')
async def root():
    return {"bot": "running"}

@app.on_event("startup")
async def on_startap():
    asyncio.create_task(run_bot())