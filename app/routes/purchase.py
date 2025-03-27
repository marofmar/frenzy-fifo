from fastapi import APIRouter, HTTPException
from app.store import decrease_stock, set_stock

router = APIRouter()

PRODUCT_ID = "product_1:한정판"

@router.post("/purchase")
async def purchase():
    success = decrease_stock(PRODUCT_ID)
    if not success:
        raise HTTPException(status_code=400, detail="재고가 없습니다.")
    return {"message": "구매 성공!"}

@router.post("/reset")
async def reset():
    set_stock(PRODUCT_ID, 100)
    return {"message": "재고 100으로 초기화 되었음."}

