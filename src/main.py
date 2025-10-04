"""Main FastAPI application for Zapdos trading bot."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import accounts, health, trading
from src.config import settings
from src.core.logging import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    # Startup
    setup_logging()
    yield
    # Shutdown
    pass


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Zapdos Trading Bot",
        description="Algorithmic trading bot using Public API",
        version=settings.APP_VERSION,
        lifespan=lifespan,
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Configure appropriately for production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(health.router, prefix="/api/v1", tags=["health"])
    app.include_router(accounts.router, prefix="/api/v1", tags=["accounts"])
    app.include_router(trading.router, prefix="/api/v1", tags=["trading"])

    return app


app = create_app()
