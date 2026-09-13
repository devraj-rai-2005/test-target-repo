from fastapi import FastAPI, HTTPException
from .schemas import TokenEntry
from .service import BlacklistService

app = FastAPI()
service = BlacklistService()

@app.post("/blacklist/add")
def add_to_blacklist(entry: TokenEntry):
    service.add_token(entry.token)
    return {"status": "success"}

@app.get("/blacklist/check/{token}")
def check_blacklist(token: str):
    return {"blacklisted": service.is_blacklisted(token)}