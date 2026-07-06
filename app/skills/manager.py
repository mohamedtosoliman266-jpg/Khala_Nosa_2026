"""
Skill Manager
"""

from typing import Any, Dict, List, Optional

from app.skills.base import BaseSkill


class SkillManager:

    def __init__(self):

        self.skills: List[BaseSkill] = []

    def register(self, skill: BaseSkill):

        self.skills.append(skill)

        self.skills.sort(
            key=lambda s: s.priority,
            reverse=True
        )

    def unregister(self, name: str):

        self.skills = [
            s
            for s in self.skills
            if s.name != name
        ]

    def get(self, name: str):

        for skill in self.skills:

            if skill.name == name:
                return skill

        return None

    def names(self):

        return [
            skill.name
            for skill in self.skills
        ]

    def handle(

        self,

        result: Dict[str, Any],

        context: Optional[Dict[str, Any]] = None,

    ):

        intent = result.get("intent", "")

        for skill in self.skills:

            if not skill.enabled:
                continue

            if not skill.can_handle(intent, context):
                continue

            context = skill.before_handle(context)

            response = skill.handle(result, context)

            return skill.after_handle(response)

        return None
