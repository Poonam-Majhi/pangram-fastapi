from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from .utils import is_pangram

app = FastAPI(
    title="Pangram Checker API",
    description="Simple API to check if a string contains all 26 english letters (a-z).",
    version="1.0.0",
)

class PangramRequest(BaseModel):
    text: str = Field(..., description="The input text to evaluate.")

class PangramResponse(BaseModel):
    isPangram: bool
    missing: list[str]

@app.get("/healthz", tags=["health"])
def healthz():
    return {"status": "ok"}

@app.get("/ispangram", response_model=PangramResponse, tags=["pangram"])
def get_is_pangram(text: str = Query(..., description="The input text to evaluate.")):
    ok, missing = is_pangram(text)
    return {"isPangram": ok, "missing": missing}

@app.post("/ispangram", response_model=PangramResponse, tags=["pangram"])
def post_is_pangram(payload: PangramRequest):
    ok, missing = is_pangram(payload.text)
    return {"isPangram": ok, "missing": missing}