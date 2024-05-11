from fastapi import APIRouter
from .controllers.firebase_controller import router as firebase_router

v1_router = APIRouter()

# Include Firebase routes
v1_router.include_router(firebase_router, prefix="/firebase", tags=["firebase"])
