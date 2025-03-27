from fastapi import APIRouter

router = APIRouter()

@router.post("/purchase")
async def purchase():
    return {"message": "구매 도전!"}

