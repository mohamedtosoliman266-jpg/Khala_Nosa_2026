"""
Base Skill for Khala Nosa
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class BaseSkill(ABC):

    name: str = "base"
    version: str = "1.0"
    priority: int = 0
    enabled: bool = True

    def can_handle(
        self,
        intent: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> bool:
        return False

    @abstractmethod
    def handle(
        self,
        result: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """
        result:
            Intent / NLP Result

        context:
            profile
            memory
            session
            logger
            engine
            ...
        """
        raise NotImplementedError

    def before_handle(
        self,
        context: Optional[Dict[str, Any]] = None,
    ):
        return context

    def after_handle(
        self,
        result: Any,
    ):
        return result

