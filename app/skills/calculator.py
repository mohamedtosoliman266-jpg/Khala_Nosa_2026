"""
Calculator Skill
"""

import re
from typing import Any, Dict, Optional

from app.skills.base import BaseSkill


class CalculatorSkill(BaseSkill):

    name = "calculator"
    version = "1.0"
    priority = 50

    def can_handle(
        self,
        intent: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> bool:

        if intent == "calculator":
            return True

        if context:

            message = context.get("message", "")

            return bool(
                re.fullmatch(
                    r"[0-9\+\-\*\/\(\)\.\s]+",
                    message
                )
            )

        return False

    def handle(
        self,
        result: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None,
    ) -> Any:

        message = context.get("message", "")

        try:

            value = eval(
                message,
                {"__builtins__": {}},
            )

            return f"الناتج = {value}"

        except Exception:

            return None

