from flask import Blueprint, request, jsonify
from services.local_storage import update_checklist_scores, get_candidate
import json
import os

assessment_bp = Blueprint("assessment", __name__)


@assessment_bp.route("/api/checklist", methods=["GET"])
def get_checklist():
    """Return the NSQF electrician checklist items."""
    checklist_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "data", "nsqf_electrician.json"
    )
    with open(checklist_path, "r") as f:
        checklist = json.load(f)
    return jsonify(checklist), 200


@assessment_bp.route("/api/checklist/<candidate_id>", methods=["POST"])
def submit_checklist(candidate_id):
    """
    Submit checklist scores for a candidate.
    Expects JSON: { "c1": 4, "c2": 3, ... }
    """
    scores = request.get_json()

    if not scores:
        return jsonify({"error": "Checklist scores are required."}), 400

    # Validate scores are 0-5
    for key, value in scores.items():
        if not isinstance(value, int) or value < 0 or value > 5:
            return jsonify({"error": f"Score for {key} must be an integer between 0 and 5."}), 400

    candidate = get_candidate(candidate_id)
    if not candidate:
        return jsonify({"error": "Candidate not found."}), 404

    update_checklist_scores(candidate_id, scores)

    return jsonify({"message": "Checklist scores saved successfully."}), 200
