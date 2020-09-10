import json

import requests
from fastapi import FastAPI, HTTPException

import schemas
from environment import env

app = FastAPI(title="Shopping List")


@app.post("/shopping_list/", response_model=schemas.ShoppingList)
def create_shopping_list(shopping_list_create: schemas.ShoppingListCreate):
    title = shopping_list_create.title
    description = "Items: "
    description += ", ".join(shopping_list_create.items)

    data = {
        "title": title,
        "description": description
    }

    response = requests.post(f"{env.todo_uri}/todo", json.dumps(data))
    try:
        response_json = response.json()
    except json.decoder.JSONDecodeError:
        HTTPException(status_code=400, detail="Error creating todo.")
    print(response.json())
    return schemas.ShoppingList(id=response_json["id"], title=title, items=shopping_list_create.items)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=env.todo_generator_port, reload=True)


