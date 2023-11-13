from fastapi import APIRouter, Response, Depends

from core.fastapi.dependencies import PermissionDependency, AllowAll
from core.helpers.redis import redis_client
import logging

health_router = APIRouter(prefix="/health", tags=["Health"])

logger = logging.getLogger("app")


@health_router.get("/", dependencies=[Depends(PermissionDependency([AllowAll]))])
async def app_healthcheck():
    return Response(status_code=200)


@health_router.get("/sentry")
async def sentry_healthcheck():
    1 / 0


@health_router.get("/redis", status_code=200)
async def redis_healthcheck():
    try:
        await redis_client.ping()
        return {"message": "Redis is up"}
    except Exception as ex:
        logger.error(ex)
        return {"message": "Redis is down"}
