import json
from pathlib import Path


class ProfileManager:

    def __init__(self, filename="profile.json"):
        self.path = Path(filename)

        if self.path.exists():
            with open(self.path, "r", encoding="utf-8") as f:
                self.profile = json.load(f)
        else:
            self.profile = {}

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(
                self.profile,
                f,
                ensure_ascii=False,
                indent=2
            )

    def set(self, key, value):
        self.profile[key] = value
        self.save()

    def get(self, key, default=None):
        return self.profile.get(key, default)

    def all(self):
        return self.profile
