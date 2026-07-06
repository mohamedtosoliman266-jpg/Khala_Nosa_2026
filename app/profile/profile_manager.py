import json
import os


class ProfileManager:

    def __init__(self, file_name="user_profile.json"):
        self.file_name = file_name
        self.data = {}
        self.load()

    def load(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
            except Exception:
                self.data = {}

    def save(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(
                self.data,
                f,
                ensure_ascii=False,
                indent=2
            )

    def set(self, key, value):
        self.data[key] = value
        self.save()

    def get(self, key, default=None):
        return self.data.get(key, default)

    def all(self):
        return self.data
