import json
import os
import uuid
from datetime import datetime

# Local JSON file to store candidates
DATA_FILE = "local_data.json"


def _load_data():
    """Load data from local JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"candidates": []}


def _save_data(data):
    """Save data to local JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def create_candidate(data):
    """Create a new candidate in local storage."""
    candidate_id = str(uuid.uuid4())[:8]
    db_data = _load_data()

    candidate = {
        "id": candidate_id,
        "name": data["name"],
        "trade": "electrician",
        "experience_text": data["experience_text"],
        "ai_suggested_level": data.get("ai_suggested_level", ""),
        "ai_justification": data.get("ai_justification", ""),
        "checklist_scores": {},
        "assessor_decision": "pending",
        "created_at": datetime.now().isoformat()
    }

    db_data["candidates"].append(candidate)
    _save_data(db_data)

    return candidate_id, candidate


def get_candidate(candidate_id):
    """Get a single candidate by ID."""
    db_data = _load_data()
    for candidate in db_data["candidates"]:
        if candidate["id"] == candidate_id:
            return candidate
    return None


def get_all_candidates():
    """Get all candidates."""
    db_data = _load_data()
    return db_data["candidates"]


def update_checklist_scores(candidate_id, scores):
    """Update checklist scores for a candidate."""
    db_data = _load_data()
    for candidate in db_data["candidates"]:
        if candidate["id"] == candidate_id:
            candidate["checklist_scores"] = scores
            _save_data(db_data)
            return True
    return False


def update_assessor_decision(candidate_id, decision):
    """Update the assessor's final decision."""
    db_data = _load_data()
    for candidate in db_data["candidates"]:
        if candidate["id"] == candidate_id:
            candidate["assessor_decision"] = decision
            _save_data(db_data)
            return True
    return False
