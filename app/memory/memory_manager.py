import json
import os


class MemoryManager:
    """
    Persistent conversation memory.
    """

    def __init__(self, max_history=20, file_name="memory.json"):
        self.max_history = max_history
        self.file_name = file_name
        self.history = []

        self.load()

    def remember_user(self, message: str):
        self.history.append({
            "role": "user",
            "text": message
        })
        self._trim()
        self.save()

    def remember_assistant(self, message: str):
        self.history.append({
            "role": "assistant",
            "text": message
        })
        self._trim()
        self.save()

    def get_history(self):
        return self.history

    def build_context(self):
        lines = []

        for item in self.history:
            if item["role"] == "user":
                lines.append(f"المستخدم: {item['text']}")
            else:
                lines.append(f"الخالة نوسة: {item['text']}")

        return "\n".join(lines)

    def clear(self):
        self.history = []
        self.save()

    def save(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(
                self.history,
                f,
                ensure_ascii=False,
                indent=2
            )

    def load(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r", encoding="utf-8") as f:
                    self.history = json.load(f)
            except Exception:
                self.history = []

    def _trim(self):
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]
