"""
Khala Nosa Engine
"""

from app.brain.brain import KhalaBrain
from app.nlu.bootstrap import create_nlu
from app.skills.profile import ProfileSkill


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

        self.nlu = create_nlu()

        self.profile_skill = ProfileSkill(profile)

        self.brain = KhalaBrain(
            memory=memory,
            profile=profile,
            skills=skills,
            ai=ai_provider,
        )

    def process(self, message: str):

        message = message.strip()

        if not message:
            return "قولي يا حبيبي محتاج إيه؟"

        if self.memory:
            self.memory.remember_user(message)

        result = self.nlu.analyze(message)

        context = {
            "message": message,
            "profile": self.profile,
            "memory": self.memory,
            "engine": self,
        }

        # جميع الـ Skills
        if self.skills:

            response = self.skills.handle(
                result,
                context,
            )

            if response:

                if self.memory:
                    self.memory.remember_assistant(response)

                return response

        # توافق مع الكود القديم
        response = self.profile_skill.handle(result)

        if response:

            if self.memory:
                self.memory.remember_assistant(response)

            return response

        prompt = ""

        if self.personality:

            prompt += self.personality.system_prompt().strip()
            prompt += "\n\n"

        if self.profile:

            data = self.profile.all()

            if data:

                prompt += "بيانات المستخدم:\n"

                for k, v in data.items():
                    prompt += f"{k}: {v}\n"

                prompt += "\n"

        if self.memory:

            history = self.memory.build_context()

            if history:

                prompt += "المحادثة السابقة:\n"
                prompt += history
                prompt += "\n\n"

        prompt += f"رسالة المستخدم:\n{message}"

        response = self.brain.think(prompt)

        if self.memory:
            self.memory.remember_assistant(response)

        return response

