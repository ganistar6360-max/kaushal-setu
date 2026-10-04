import firebase_admin
from firebase_admin import credentials, firestore
import os
import uuid
from dotenv import load_dotenv

load_dotenv()

# Initialize Firebase Admin SDK
# Place your Firebase service account key JSON file in backend/ and set the env var
cred_path = os.getenv("FIREBASE_CREDENTIALS", "serviceAccountKey.json")

if not firebase_admin._apps:
    if os.path.exists(cred_path):
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
    else:
        # Fallback: initialize without credentials (works with FIREBASE_APPLICATION_CREDENTIALS env)
        firebase_admin.initialize_app()

db = firestore.client()


def create_candidate(data):
    """Create a new candidate document in Firestore."""
    candidate_id = str(uuid.uuid4())[:8]
    doc_ref = db.collection("candidates").document(candidate_id)
    doc_data = {
        "name": data["name"],
        "trade": "electrician",
        "experience_text": data["experience_text"],
        "ai_suggested_level": data.get("ai_suggested_level", ""),
        "ai_justification": data.get("ai_justification", ""),
        "checklist_scores": {},
        "assessor_decision": "pending",
    }
    doc_ref.set(doc_data)
    return candidate_id, doc_data


def get_candidate(candidate_id):
    """Get a single candidate by ID."""
    doc = db.collection("candidates").document(candidate_id).get()
    if doc.exists:
        data = doc.to_dict()
        data["id"] = doc.id
        return data
    return None


def get_all_candidates():
    """Get all candidates."""
    docs = db.collection("candidates").stream()
    candidates = []
    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        candidates.append(data)
    return candidates


def update_checklist_scores(candidate_id, scores):
    """Update checklist scores for a candidate."""
    doc_ref = db.collection("candidates").document(candidate_id)
    doc_ref.update({"checklist_scores": scores})
    return True


def update_assessor_decision(candidate_id, decision):
    """Update the assessor's final decision."""
    doc_ref = db.collection("candidates").document(candidate_id)
    doc_ref.update({"assessor_decision": decision})
    return True
