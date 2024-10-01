import uuid

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class Item(ItemBase):
    id: uuid.UUID

    class Config:
        orm_mode = True


class ItemCreate(ItemBase):
    pass
