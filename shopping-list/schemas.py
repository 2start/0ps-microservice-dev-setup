from typing import List

from pydantic import BaseModel


class ShoppingListCreate(BaseModel):
    title: str
    items: List[str]
    
    class Config:
        schema_extra = {
            "example": {
                "title": "My first shopping list",
                "items": [
                    "item1",
                    "item2",
                    "item3",
                ]
            }
        }


class ShoppingList(BaseModel):
    id: int
    title: str
    items: List[str]
