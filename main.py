from fastapi import FastAPI
from model import User

app = FastAPI(title="Backend Hard")


@app.get("/calculate")
def calc(num1: float, num2: float):
    return {"result": num1 + num2}


@app.post("/user")
def is_user_adult(user: User):
    if user.age >= 18:
        is_adult = True
    else:
        is_adult = False

    return {**user.dict(), "is_adult": is_adult}
