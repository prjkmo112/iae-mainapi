import os
import socket
import yaml
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from module.logger import logger
import module.utils as utils


with open(os.path.join(os.path.dirname(__file__), 'config/main.yaml'), 'r') as f:
    CONFIG = yaml.safe_load(f.read())

app = FastAPI(
    title=CONFIG["app"]['title'],
    description=CONFIG['app']['description'],
    summary=CONFIG['app']['summary'],
    version=CONFIG['app']['version'],
)

# routers

# middleware
## default middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## custom middleware
def ipblocker_middleware(request: Request, next):
    client_ip = request.client.host
    logger.info(f"Client IP: {client_ip}")

    # Check if the IP is blocked
    if client_ip in CONFIG["blocked_ips"]:
        logger.warning(f"Blocked IP: {client_ip}")
        raise HTTPException(status_code=403, detail="Forbidden")

def logger_middleware(req:Request, next):
    logger.info(f"Request: {req.method}|{req.url}")

@app.middleware("http")
async def custom_middleware(req: Request, next):
    # ipblocker_middleware(req, next)
    logger_middleware(req, next)

    response = await next(req)
    return response

@app.get("/")
async def root():
    return {"message": "Welcome to the IAE Main API!"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/version")
async def version():
    return {"version": CONFIG['app']['version']}