from fastapi import APIRouter

router = APIRouter()

@router.post("/purchase")
async def purchase():
    return {"message": "Purchase attempted"}

