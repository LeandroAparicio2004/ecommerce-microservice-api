from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int

class ProductResponse(ProductCreate):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    customer_name: str
    customer_email: str
    items: List[OrderItemCreate]

class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    unit_price: float
    class Config:
        from_attributes = True

class OrderResponse(BaseModel):
    id: int
    customer_name: str
    customer_email: str
    status: str
    created_at: datetime
    items: List[OrderItemResponse]
    class Config:
        from_attributes = True