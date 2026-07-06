import re


class CalculatorSkill:

    def can_handle(self, message):

        return bool(
            re.fullmatch(
                r"[0-9\+\-\*\/\(\)\.\s]+",
                message
            )
        )

    def handle(self, message):

        try:
            result = eval(message, {"__builtins__": {}})
            return f"الناتج = {result}"
        except Exception:
            return None

