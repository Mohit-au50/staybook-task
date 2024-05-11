from fastapi import FastAPI
from .v1.routes.firebase_routes import v1_router
import uvicorn

app = FastAPI()

# Test route
@app.get("/")
async def test_route():
    return {"name": "test", "message": "satybook FastAPI is working"}

# Include v1 router
app.include_router(v1_router, prefix="/api/v1/hotels")

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
