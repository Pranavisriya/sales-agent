# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os


from agent import answer 

# -------- FastAPI app --------
app = FastAPI(title="Sales Agent API" )

class AnswerIn(BaseModel):
    thread_id: str
    user_text: str

class AnswerOut(BaseModel):
    reply: str

@app.get("/")
def greet():
    return {"message": "Welcome to the Sales Agent API!"}

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/answer", response_model=AnswerOut)
def post_answer(payload: AnswerIn):
    resp = answer(payload.thread_id, payload.user_text)
    return {"reply": resp}
