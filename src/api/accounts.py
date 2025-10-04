"""Account management endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/accounts")
async def get_accounts():
    """Get all accounts - placeholder."""
    return {"message": "Accounts endpoint - not implemented yet"}
