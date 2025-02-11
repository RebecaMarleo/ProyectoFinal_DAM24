from fastapi import FastAPI
import uvicorn
from app.routers import client, product, sale, product_sale
from app.db.database import Base, engine

def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()

app = FastAPI()
app.include_router(client.router)
app.include_router(product.router)
app.include_router(sale.router)
app.include_router(product_sale.router)

if __name__=="__main__":
    uvicorn.run("main:app", port=8000, reload=True)
