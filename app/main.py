from fastapi import FastAPI
from app.routes import purchase, stats

app = FastAPI()

app.include_router(purchase.router)
app.include_router(stats.router)


