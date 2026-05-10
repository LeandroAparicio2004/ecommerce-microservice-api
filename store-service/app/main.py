from fastapi import FastAPI
from app.database import Base, engine
from app.routers import products, orders
import time
import sqlalchemy

def wait_for_db():
    retries = 10
    while retries > 0:
        try:
            with engine.connect():
                print("Base de datos lista!")
                break
        except sqlalchemy.exc.OperationalError:
            print("Esperando base de datos...")
            retries -= 1
            time.sleep(3)

wait_for_db()
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce API",
    description="API REST para gestión de productos y órdenes de compra",
    version="1.0.0"
)

app.include_router(products.router)
app.include_router(orders.router)

@app.get("/")
def root():
    return {"message": "E-Commerce API corriendo correctamente"}