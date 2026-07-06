"""
Khala Nosa Engine
"""

from app.brain.brain import KhalaBrain
from app.nlu.bootstrap import create_nlu


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

        self.brain = KhalaBrain(
            memory=memory,
            profile=profile,
            skills=skills,
            ai=ai_provider,
        )

    def process(self, message: str) -> str:

        if not message.strip():
            return "قولي يا حبيبي محتاج إيه؟"

        if self.memory:
            self.memory.remember_user(message)

        result = self.nlu.analyze(message)

        # الاسم
        if result["intent"] == "save_name":
            self.profile.set("name", result["value"])
            response = f"تشرفت بيك يا {result['value']} 🌸"

        elif result["intent"] == "ask_name":
            name = self.profile.get("name")
            response = f"اسمك {name} 🌸" if name else "لسه ماعرفش اسمك."

        # العمر
        elif result["intent"] == "save_age":
            self.profile.set("age", result["value"])
            response = f"تمام... سجلت إن عمرك {result['value']} سنة 🌸"

        elif result["intent"] == "ask_age":
            age = self.profile.get("age")
            response = f"عمرك {age} سنة 🌸" if age is not None else "لسه معرفش عمرك."

        # المهنة
        elif result["intent"] == "save_job":
            self.profile.set("job", result["value"])
            response = f"تمام... سجلت إن شغلك {result['value']} 🌸"

        elif result["intent"] == "ask_job":
            job = self.profile.get("job")
            response = f"أنت بتشتغل {job} 🌸" if job else "لسه معرفش شغلك."

        # المدينة
        elif result["intent"] == "save_city":
            self.profile.set("city", result["value"])
            response = f"تمام... سجلت إنك ساكن في {result['value']} 🌸"

        elif result["intent"] == "ask_city":
            city = self.profile.get("city")
            response = f"أنت ساكن في {city} 🌸" if city else "لسه معرفش ساكن فين."

        # احكيلي عني
        elif result["intent"] == "about_me":

            profile = self.profile.all()

            response = (
                f"👤 اسمك: {profile.get('name', 'غير معروف')}\n"
                f"🎂 عمرك: {profile.get('age', 'غير معروف')}\n"
                f"💼 شغلك: {profile.get('job', 'غير معروف')}\n"
                f"🏠 ساكن في: {profile.get('city', 'غير معروف')}"
            )

        else:

            prompt = ""

            if self.personality:
                prompt += self.personality.system_prompt().strip()
                prompt += "\n\n"

            if self.profile:
                profile = self.profile.all()

                if profile:
                    prompt += "بيانات المستخدم:\n"

                    for key, value in profile.items():
                        prompt += f"{key}: {value}\n"

                    prompt += "\n"

            if self.memory:
                history = self.memory.build_context()

                if history:
                    prompt += "المحادثة السابقة:\n"
                    prompt += history
                    prompt += "\n\n"

            prompt += "رسالة المستخدم:\n"
            prompt += message

            response = self.brain.think(prompt)

        if self.memory:
            self.memory.remember_assistant(response)

        return response

