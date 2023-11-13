from fastapi import APIRouter

from api.user.v1.user import user_router as user_v1_router
from api.auth.auth import auth_router

router_v1 = APIRouter(prefix="/api/v1")
router_v1.include_router(user_v1_router, prefix="/users", tags=["User"])
router_v1.include_router(auth_router, prefix="/auth", tags=["Auth"])

router = APIRouter()
router.include_router(router_v1)

__all__ = ["router"]
