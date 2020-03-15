from typing import Dict, Callable
from app.cli import get_starting_text


def follow_all(commented_actions: Dict[Callable, str]) -> None:
    for action, comment in commented_actions.items():
        print(get_starting_text(comment))
        action()
