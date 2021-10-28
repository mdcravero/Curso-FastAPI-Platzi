from fastapi import FastAPI

app = FastAPI()


@app.get("/")  # Path operation decorator
def home():  # Path operaton function
    return {"Hello": "World"}
