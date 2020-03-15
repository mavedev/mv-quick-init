from typing import Dict, Callable
from time import sleep
from app.cli import get_starting_text
from .constants import _STEP_DELAY_SECONDS


def follow_all(commented_actions: Dict[Callable, str]) -> None:
    for action, comment in commented_actions.items():
        print(get_starting_text(comment))
        action()
        sleep(_STEP_DELAY_SECONDS)
