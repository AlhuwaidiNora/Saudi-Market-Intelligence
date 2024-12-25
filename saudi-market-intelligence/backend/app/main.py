from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import market_data, analysis, auth, users

app = FastAPI(
    title="Saudi Market Intelligence API",
    description="API for Saudi market analysis and intelligence",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(market_data.router, prefix="/api/market-data", tags=["Market Data"])
app.include_router(analysis.router, prefix="/api/analysis", tags=["Analysis"])

@app.get("/")
async def root():
    return {"message": "Welcome to Saudi Market Intelligence API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
