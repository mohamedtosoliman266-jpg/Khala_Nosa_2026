"""
Khala Nosa Engine

The central coordinator of the application.
It does not contain AI logic.
It only coordinates the processing pipeline.
"""


class Engine:
    def __init__(
        self,
        personality=None,
        memory=None,
        skills=None,
        ai_provider=None,
    ):
        self.personality = personality
        self.memory = memory
        self.skills = skills
        self.ai_provider = ai_provider

    def process(self, message: str) -> str:
        """
        Main processing pipeline.
        """

        if not message.strip():
            return "قولي يا حبيبي محتاج إيه؟"

        # Memory (future)
        if self.memory:
            self.memory.remember(message)

        # Skills (future)
        if self.skills:
            result = self.skills.handle(message)
            if result:
                return result

        # AI Provider
        if self.ai_provider:
            return self.ai_provider.generate(message)

        # Default response
        return (
            "أنا الخالة نوسة 🌸\n"
            "لسه بتكبر وبتتعلم.\n"
            "استنى عليا شوية وهبقى أشطر واحدة."
        )
