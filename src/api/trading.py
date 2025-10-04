"""Trading operations endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/trading")
async def get_trading_info():
    """Get trading info - placeholder."""
    return {"message": "Trading endpoint - not implemented yet"}
