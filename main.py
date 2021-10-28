# Python
from typing import Optional
import fastapi

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

# Models


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    # Datos opcionales, si el usuario no ingresa nada queda en None
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get("/")  # Path operation decorator
def home():  # Path operaton function
    return {"Hello": "World"}

# Request and Response Body


@app.post("/person/new")
# Los 3 puntos indican que es obligatorio (required)
def create_person(person: Person = Body(...)):
    return person
