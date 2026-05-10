from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Order, OrderItem, Product
from app.schemas.schemas import OrderCreate, OrderResponse
from typing import List
import redis
import json
import os

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_redis():
    return redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, decode_responses=True)

@router.get("/", response_model=List[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return order

@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(customer_name=order.customer_name, customer_email=order.customer_email)
    db.add(db_order)
    db.flush()

    for item in order.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Producto {item.product_id} no encontrado")
        if product.stock < item.quantity:
            raise HTTPException(status_code=400, detail=f"Stock insuficiente para {product.name}")
        product.stock -= item.quantity
        db_item = OrderItem(order_id=db_order.id, product_id=item.product_id,
                            quantity=item.quantity, unit_price=product.price)
        db.add(db_item)

    db.commit()
    db.refresh(db_order)

    try:
        r = get_redis()
        r.publish("new_order", json.dumps({
            "order_id": db_order.id,
            "customer_name": db_order.customer_name,
            "customer_email": db_order.customer_email,
            "status": db_order.status
        }))
    except Exception:
        pass

    return db_order