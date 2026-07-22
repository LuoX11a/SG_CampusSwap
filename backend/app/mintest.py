"""
MINIMAL test app — deploy this to verify Render infrastructure works.
"""
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
@app.get("/health")
async def health():
    return {"status": "ok"}
