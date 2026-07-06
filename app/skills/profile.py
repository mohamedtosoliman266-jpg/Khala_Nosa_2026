from typing import Any, Dict, Optional

from app.skills.base import BaseSkill


class ProfileSkill(BaseSkill):

    name = "profile"
    priority = 100

    def __init__(self, profile):
        self.profile = profile

    def can_handle(self, intent: str, context=None):
        return (
            intent.startswith("save_")
            or intent.startswith("ask_")
            or intent in ("about_me", "save_fact")
        )

    def handle(
        self,
        result: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None,
    ) -> Any:

        intent = result["intent"]

        if intent == "save_fact":

            self.profile.set(
                result["key"],
                result["value"],
            )

            return "تمام... افتكرتها 🌸"

        if intent == "save_name":
            self.profile.set("name", result["value"])
            return f"تشرفت بيك يا {result['value']} 🌸"

        if intent == "ask_name":
            name = self.profile.get("name")
            return f"اسمك {name} 🌸" if name else "لسه معرفش اسمك."

        if intent == "save_age":
            self.profile.set("age", result["value"])
            return f"تمام... سجلت إن عمرك {result['value']} سنة 🌸"

        if intent == "ask_age":
            age = self.profile.get("age")
            return f"عمرك {age} سنة 🌸" if age else "لسه معرفش عمرك."

        if intent == "save_job":
            self.profile.set("job", result["value"])
            return f"تمام... سجلت إن شغلك {result['value']} 🌸"

        if intent == "ask_job":
            job = self.profile.get("job")
            return f"أنت بتشتغل {job} 🌸" if job else "لسه معرفش شغلك."

        if intent == "save_city":
            self.profile.set("city", result["value"])
            return f"تمام... سجلت إنك ساكن في {result['value']} 🌸"

        if intent == "ask_city":
            city = self.profile.get("city")
            return f"أنت ساكن في {city} 🌸" if city else "لسه معرفش ساكن فين."

        if intent == "about_me":

            p = self.profile.all()

            text = (
                f"👤 اسمك: {p.get('name','غير معروف')}\n"
                f"🎂 عمرك: {p.get('age','غير معروف')}\n"
                f"💼 شغلك: {p.get('job','غير معروف')}\n"
                f"🏠 ساكن في: {p.get('city','غير معروف')}\n\n"
            )

            extras = {
                "likes": "❤️ يحب",
                "dislikes": "💔 يكره",
                "favorite_color": "🎨 اللون المفضل",
                "car": "🚗 العربية",
                "wife": "💍 الزوجة",
                "son": "👦 الابن",
                "daughter": "👧 البنت",
            }

            for key, title in extras.items():

                if key in p:
                    text += f"{title}: {p[key]}\n"

            return text.strip()

        return None

