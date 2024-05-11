from ..database.firebase import db
from fastapi import APIRouter, HTTPException

router = APIRouter()

# Define route to get all Firebase documents
@router.get("/")
async def get_all_firebase_documents():
    try:
        documents = [doc.to_dict() for doc in db.collection("your_collection").get()]
        return {"status": "OK", "data": documents}
    except Exception as e:
        raise HTTPException(status_code=500, detail={"status": "FAILED", "data": {"error": str(e)}})
