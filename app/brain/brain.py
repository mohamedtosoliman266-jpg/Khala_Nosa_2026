from app.brain.router import IntentRouter


class KhalaBrain:

    def __init__(
        self,
        memory=None,
        profile=None,
        skills=None,
        ai=None,
    ):
        self.memory = memory
        self.profile = profile
        self.skills = skills
        self.ai = ai

        self.router = IntentRouter()

    def think(self, prompt):

        skill = self.skills.find(prompt)

        if skill:
            return skill.handle(prompt)

        if self.ai:
            return self.ai.generate(prompt)

        return "أنا الخالة نوسة 🌸"
