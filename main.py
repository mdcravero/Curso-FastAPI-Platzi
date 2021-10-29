# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

# Models


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    # Datos opcionales, si el usuario no ingresa nada queda en None
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


class Location (BaseModel):
    city: str
    state: str
    country: str


@app.get("/")  # Path operation decorator
def home():  # Path operaton function
    return {"Hello": "World"}

# Request and Response Body


@app.post("/person/new")
# Los 3 puntos indican que es obligatorio (required)
def create_person(person: Person = Body(...)):
    return person

# Validations: Query Parameters


@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="This is a person name. It's between 1 and 50 characters"
    ),
    age: Optional[str] = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required"
    )
):
    return{name: age}

# Validations Path Parameters


@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person Id",
        description="This is a person Id. It's required"
    )  # Con gt validamos que sea mayor a 0
):
    return {person_id: "It exists!"}

# Validations Request Body


@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person Id",
        description="This is the person Id",
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    result = person.dict()
    # Convierto a diccionario y uno los person y location
    result.update(location.dict())

    return result
