"""
Khala Nosa Engine
"""


class Engine:

    def __init__(
        self,
        personality=None,
        memory=None,
        profile=None,
        skills=None,
        ai_provider=None,
    ):
        self.personality = personality
        self.memory = memory
        self.profile = profile
        self.skills = skills
        self.ai_provider = ai_provider

    def process(self, message: str) -> str:

        if not message.strip():
            return "قولي يا حبيبي محتاج إيه؟"

        if self.memory:
            self.memory.remember_user(message)

        if self.skills:
            result = self.skills.handle(message)
            if result:
                if self.memory:
                    self.memory.remember_assistant(result)
                return result

        prompt = ""

        # Personality
        if self.personality:
            prompt += self.personality.system_prompt().strip()
            prompt += "\n\n"

        # User Profile
        if self.profile:
            data = self.profile.all()

            if data:
                prompt += "بيانات المستخدم:\n"

                for k, v in data.items():
                    prompt += f"{k}: {v}\n"

                prompt += "\n"

        # Conversation Memory
        if self.memory:
            history = self.memory.build_context()

            if history:
                prompt += "المحادثة السابقة:\n"
                prompt += history
                prompt += "\n\n"

        prompt += "رسالة المستخدم:\n"
        prompt += message

        if self.ai_provider:
            response = self.ai_provider.generate(prompt)
        else:
            response = "أنا الخالة نوسة 🌸"

        if self.memory:
            self.memory.remember_assistant(response)

        return response
