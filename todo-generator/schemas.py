from typing import List

from pydantic import BaseModel


class ShoppingListCreate(BaseModel):
    title: str
    items: List[str]


class ShoppingList(BaseModel):
    id: int
    title: str
    items: List[str]
