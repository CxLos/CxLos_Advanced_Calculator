# app/auth/redis_client.py
import redis.asyncio as aioredis  # pragma: no cover
from app.core.config import get_settings  # pragma: no cover

settings = get_settings()  # pragma: no cover

async def get_redis():  # pragma: no cover
    if not hasattr(get_redis, "redis"):  # pragma: no cover
        get_redis.redis = await aioredis.from_url(  # pragma: no cover
            settings.REDIS_URL or "redis://localhost"  # pragma: no cover
        )  # pragma: no cover
    return get_redis.redis  # pragma: no cover

async def add_to_blacklist(jti: str, exp: int):  # pragma: no cover
    """Add a token's JTI to the blacklist"""
    redis = await get_redis()  # pragma: no cover
    await redis.set(f"blacklist:{jti}", "1", ex=exp)  # pragma: no cover

async def is_blacklisted(jti: str) -> bool:  # pragma: no cover
    """Check if a token's JTI is blacklisted"""
    redis = await get_redis()  # pragma: no cover
    return await redis.exists(f"blacklist:{jti}")  # pragma: no cover