from fastapi import APIRouter
from app.store import get_stats

router = APIRouter()

@router.get("/stats")
async def stats():
    return get_stats()
