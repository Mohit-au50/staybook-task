import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase credentials from JSON file
cred = credentials.Certificate("firebaseConfig.json")

# Initialize Firebase Admin SDK
firebase_admin.initialize_app(cred)

# Access Firestore instance
db = firestore.client()
