class SkillManager:

    def __init__(self):
        self.skills = []

    def register(self, skill):
        self.skills.append(skill)

    def find(self, message):

        for skill in self.skills:

            if skill.can_handle(message):
                return skill

        return None
