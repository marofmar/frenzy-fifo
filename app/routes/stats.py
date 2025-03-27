from fastapi import APIRouter

router = APIRouter()

@router.get("/stats")
async def stats():
    return {"sucess": 0, "fail": 0}