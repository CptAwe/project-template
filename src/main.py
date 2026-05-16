import uvicorn
from loguru import logger
from fastapi import FastAPI

from config import *
appsettings = Settings.appSettings()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    
    if Settings.appSettings.debug_mode:
        logger.info(f"Running in debug mode")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        **appsettings.additional_settings
    )
