from flask import Blueprint, request, jsonify
from services.local_storage import create_candidate
from services.local_ai import get_nsqf_level

declaration_bp = Blueprint("declaration", __name__)


@declaration_bp.route("/api/declare", methods=["POST"])
def submit_declaration():
    """
    Accepts a self-declaration form submission.
    Saves the candidate to Firestore and runs AI skill mapping.
    """
    data = request.get_json()

    if not data or not data.get("name") or not data.get("experience_text"):
        return jsonify({"error": "Name and experience text are required."}), 400

    # Run AI mapping
    ai_result = get_nsqf_level(data["experience_text"])

    candidate_data = {
        "name": data["name"],
        "experience_text": data["experience_text"],
        "ai_suggested_level": ai_result["suggested_level"],
        "ai_justification": ai_result["justification"],
    }

    candidate_id, saved_data = create_candidate(candidate_data)

    return jsonify({
        "message": "Declaration submitted successfully.",
        "candidate_id": candidate_id,
        "ai_suggested_level": ai_result["suggested_level"],
        "ai_justification": ai_result["justification"],
    }), 201
