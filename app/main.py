from fastapi import FastAPI
import logging

logger = logging.getLogger(__name__)
app = FastAPI()
logger.info("Hello world")

@app.get("/")
async def root():
    return {"message": "Hello World"}
