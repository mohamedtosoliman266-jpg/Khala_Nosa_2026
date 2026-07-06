from pathlib import Path

from flask import Flask, request, jsonify, render_template

from app.core.engine import Engine
from app.ai.providers.gemini_provider import GeminiProvider
from app.memory.memory_manager import MemoryManager
from app.personalities.khala_nosa import KhalaNosaPersonality
from app.profile.profile_manager import ProfileManager

BASE_DIR = Path(__file__).resolve().parents[2]

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates")
)

ai = GeminiProvider()
memory = MemoryManager()
personality = KhalaNosaPersonality()
profile = ProfileManager()

engine = Engine(
    ai_provider=ai,
    memory=memory,
    personality=personality,
    profile=profile,
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json or {}
    message = data.get("message", "")

    response = engine.process(message)

    return jsonify({
        "response": response
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
