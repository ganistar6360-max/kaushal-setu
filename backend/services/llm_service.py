import json
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def get_nsqf_level(experience_text, nsqf_pack_path="data/nsqf_electrician.json"):
    """
    Sends the worker's experience text and the NSQF checklist to Gemini
    and returns the AI-suggested NSQF level with justification.
    """
    with open(nsqf_pack_path, "r") as f:
        nsqf_pack = json.load(f)

    nsqf_pack_str = json.dumps(nsqf_pack, indent=2)

    prompt = (
        f"You are an expert skill assessor for the Indian National Skills Qualification Framework (NSQF).\n\n"
        f"NSQF Qualification Pack for Electrician trade:\n{nsqf_pack_str}\n\n"
        f"Worker's self-declared experience:\n{experience_text}\n\n"
        f"Based on this, suggest the closest matching NSQF competency level "
        f"(Level 1 to Level 5) and briefly justify why in 2-3 sentences.\n\n"
        f"Respond in this exact JSON format:\n"
        f'{{"suggested_level": "NSQF Level X", "justification": "Your 2-3 sentence justification here."}}\n\n'
        f"Return ONLY the JSON, no other text."
    )

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()

        # Strip markdown code fences if present
        if text.startswith("```"):
            text = text.split("\n", 1)[1]
            text = text.rsplit("```", 1)[0].strip()

        result = json.loads(text)
        return {
            "suggested_level": result.get("suggested_level", "Unknown"),
            "justification": result.get("justification", "No justification provided."),
        }
    except Exception as e:
        return {
            "suggested_level": "Error",
            "justification": f"AI assessment failed: {str(e)}",
        }
