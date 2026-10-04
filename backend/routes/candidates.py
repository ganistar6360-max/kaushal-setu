from flask import Blueprint, jsonify, request
from services.local_storage import get_all_candidates, get_candidate, update_assessor_decision

candidates_bp = Blueprint("candidates", __name__)


@candidates_bp.route("/api/candidates", methods=["GET"])
def list_candidates():
    """Return all candidates for the assessor dashboard."""
    candidates = get_all_candidates()
    return jsonify(candidates), 200


@candidates_bp.route("/api/candidates/<candidate_id>", methods=["GET"])
def get_single_candidate(candidate_id):
    """Return a single candidate by ID."""
    candidate = get_candidate(candidate_id)
    if not candidate:
        return jsonify({"error": "Candidate not found."}), 404
    return jsonify(candidate), 200


@candidates_bp.route("/api/candidates/<candidate_id>/decision", methods=["POST"])
def submit_decision(candidate_id):
    """
    Submit assessor's final decision for a candidate.
    Expects JSON: { "decision": "approved" | "overridden" }
    """
    data = request.get_json()

    if not data or data.get("decision") not in ("approved", "overridden"):
        return jsonify({"error": "Decision must be 'approved' or 'overridden'."}), 400

    candidate = get_candidate(candidate_id)
    if not candidate:
        return jsonify({"error": "Candidate not found."}), 404

    update_assessor_decision(candidate_id, data["decision"])

    return jsonify({
        "message": f"Decision '{data['decision']}' recorded for {candidate['name']}.",
    }), 200
