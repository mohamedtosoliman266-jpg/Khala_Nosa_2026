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

    def think(self, prompt):

        if self.ai:
            return self.ai.generate(prompt)

        return "أنا الخالة نوسة 🌸"
