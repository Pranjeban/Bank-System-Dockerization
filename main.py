from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

json_file_path = "users.json"

if not os.path.exists(json_file_path):
    with open(json_file_path, "w") as file:
        json.dump([], file)

class User(BaseModel):
    account_id: int
    name: str
    current_balance: float

@app.post("/add_user")
async def add_user(user: User):
    with open(json_file_path, "r+") as file:
        users = json.load(file)
        users.append(user.dict())
        file.seek(0)
        json.dump(users, file, indent=4)
    return {"message": "User added successfully"}

@app.get("/get_user/{account_id}")
async def get_user(account_id: int):
    with open(json_file_path, "r") as file:
        users = json.load(file)
        for user in users:
            if user["account_id"] == account_id:
                return user
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/")
async def serve_static():
    return HTMLResponse(open("static/index.html").read())

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
