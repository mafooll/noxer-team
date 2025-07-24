from pydantic import BaseModel
from typing import Optional


class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    image_url: Optional[str]
    on_main: bool
    category: Optional[str]
