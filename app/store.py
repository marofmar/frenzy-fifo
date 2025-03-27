import redis
from typing import Optional

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def get_redis_client():
    return r

def set_stock(product_id: str, stock: int):
    r.set(f"stock:{product_id}", stock)

def get_stock(product_id: str) -> Optional[int]:
    val = r.get(f"stock:{product_id}")
    return int(val) if val else None

def decrease_stock(product_id: str) -> bool:
    pipe = r.pipeline()  # https://redis.io/docs/latest/develop/use/pipelining/
    while True:
        try:
            pipe.watch(f"stock:{product_id}")
            current_stock = int(pipe.get(f"stock:{product_id}"))
            if current_stock <= 0:
                pipe.unwatch()
                return False
            pipe.multi()
            pipe.decr(f"stock:{product_id}")
            pipe.execute()
            return True
        except redis.WatchError:
            continue  # 다시 시도

def increment_success():
    r.incr("success")

def increment_fail():
    r.incr("fail")

def get_stats():
    success = int(r.get("success") or 0)
    fail = int(r.get("fail") or 0)
    return {"success": success, "fail": fail}

