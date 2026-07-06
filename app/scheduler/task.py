from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:

    id: str

    title: str

    run_at: datetime

    action: str

    done: bool = False
