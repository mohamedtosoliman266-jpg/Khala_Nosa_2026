from app.core.engine import Engine
from app.ai.providers.gemini_provider import GeminiProvider
from app.memory.memory_manager import MemoryManager
from app.personalities.khala_nosa import KhalaNosaPersonality
from app.profile.profile_manager import ProfileManager

from app.skills.manager import SkillManager
from app.skills.calculator import CalculatorSkill


def main():
    ai = GeminiProvider()

    memory = MemoryManager()

    personality = KhalaNosaPersonality()

    profile = ProfileManager()

    skills = SkillManager()
    skills.register(CalculatorSkill())

    engine = Engine(
        ai_provider=ai,
        memory=memory,
        personality=personality,
        profile=profile,
        skills=skills,
    )

    print("🌸 Khala Nosa 2026")
    print("اكتب exit للخروج.\n")

    while True:

        msg = input("أنت: ")

        if msg.lower() in ("exit", "quit"):
            print("الخالة نوسة: مع السلامة 🌷")
            break

        response = engine.process(msg)

        print("الخالة نوسة:", response)


if __name__ == "__main__":
    main()
