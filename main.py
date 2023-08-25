from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional



app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RainData:
    data = {}

class Rain(BaseModel):
    rain: int
    
class User(BaseModel):
    username: str
    password: str

users_db = {}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/rains")
def receive_rain(data: Rain):
    if data.rain is not None:
        RainData.data = {"rain": data.rain}
        return {"message": "Rain data received"}
    else:
        raise HTTPException(status_code=400, detail="rain field is missing")

@app.get("/show_rain")
def show_rain():
    if "rain" in RainData.data:
        return RainData.data
    else:
        return {"message": "Rain data not available"}


@app.post("/login")
async def login(user: User):
    stored_password = users_db.get(user.username)
    if stored_password is None or stored_password != user.password:
        return {"message": "Invalid credentials"}
    return {"username": user.username, "message": "Login successful"}

@app.post("/signup")
async def signup(user: User):
    if user.username in users_db:
        return {"message": "Username already exists"}
    
    users_db[user.username] = user.password
    return {"Sign up successful"}




