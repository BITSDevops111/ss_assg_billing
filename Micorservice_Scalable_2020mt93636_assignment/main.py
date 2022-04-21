import uvicorn
from models import User as ModelUser
from schema import User as SchemaUser
from app import app
from db import db


@app.post("/billing/")
async def biiling_user(user: SchemaUser):
    user_id = await ModelUser.create(**user.dict())
    return {"user_id": user_id}


@app.get("/billing/{id}", response_model=SchemaUser)
async def get_billing(id: int):
    user = await ModelUser.get(id)
    return SchemaUser(**user).dict()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
