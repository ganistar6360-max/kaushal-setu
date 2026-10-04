import json
import re


def get_nsqf_level(experience_text, nsqf_pack_path="data/nsqf_electrician.json"):
    """
    Local keyword-based AI replacement for NSQF level suggestion.
    Analyzes experience text for keywords and suggests appropriate level.
    """

    # Load NSQF pack for reference
    with open(nsqf_pack_path, "r", encoding="utf-8") as f:
        nsqf_pack = json.load(f)

    # Convert to lowercase for matching
    text_lower = experience_text.lower()

    # Extract years of experience
    years_match = re.search(r'(\d+)\s*year', text_lower)
    years_experience = int(years_match.group(1)) if years_match else 0

    # Define keyword patterns for different levels
    level_5_keywords = [
        'supervise', 'manage', 'train', 'mentor', 'lead', 'oversee',
        'design', 'plan', 'coordinate', 'independent', 'complex projects',
        'industrial', 'commercial', 'contractor', 'business'
    ]

    level_4_keywords = [
        'distribution board', 'circuit diagram', 'troubleshoot', 'multimeter',
        'earthing', 'testing', 'safety code', 'advanced', 'install',
        'repair', 'maintenance', 'read diagram', 'electrical panel'
    ]

    level_3_keywords = [
        'wiring', 'basic', 'wire', 'connection', 'switch', 'socket',
        'simple', 'house', 'residential', 'helper', 'assistant',
        'basic electrical', 'plug', 'light fitting'
    ]

    level_2_keywords = [
        'apprentice', 'learning', 'beginner', 'trainee', 'observe',
        'assist', 'help', 'basic tasks', 'simple work'
    ]

    # Count keyword matches
    level_5_count = sum(1 for kw in level_5_keywords if kw in text_lower)
    level_4_count = sum(1 for kw in level_4_keywords if kw in text_lower)
    level_3_count = sum(1 for kw in level_3_keywords if kw in text_lower)
    level_2_count = sum(1 for kw in level_2_keywords if kw in text_lower)

    # Decision logic
    if level_5_count >= 2 or years_experience >= 10:
        level = "NSQF Level 5"
        justification = (
            f"Based on {years_experience} years of experience and advanced skills like "
            f"supervision, management, and complex project handling, this worker demonstrates "
            f"competencies aligned with NSQF Level 5 (skilled professional capable of independent work)."
        )
    elif level_4_count >= 2 or (years_experience >= 4 and level_4_count >= 1):
        level = "NSQF Level 4"
        justification = (
            f"With {years_experience} years of experience and skills in distribution boards, "
            f"circuit diagrams, troubleshooting, and safety compliance, this worker shows "
            f"competencies matching NSQF Level 4 (skilled worker with technical knowledge)."
        )
    elif level_3_count >= 2 or (years_experience >= 2 and level_3_count >= 1):
        level = "NSQF Level 3"
        justification = (
            f"With {years_experience} years of experience in basic wiring, installations, and "
            f"residential electrical work, this worker demonstrates NSQF Level 3 competencies "
            f"(semi-skilled worker with practical knowledge)."
        )
    elif level_2_count >= 1 or years_experience < 2:
        level = "NSQF Level 2"
        justification = (
            f"As someone with {years_experience} years of experience in basic electrical tasks, "
            f"this worker is best matched to NSQF Level 2 (basic operations under supervision)."
        )
    else:
        # Default fallback
        level = "NSQF Level 3"
        justification = (
            f"Based on the provided experience description, this worker shows foundational "
            f"electrical skills suitable for NSQF Level 3 (semi-skilled worker)."
        )

    return {
        "suggested_level": level,
        "justification": justification
    }
