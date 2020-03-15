from time import sleep
from app.cli import (
    get_starting_text,
    get_finaling_text
)
from .constants import (
    Scenario,
    _STEP_DELAY_SECONDS,
    _ON_CONFIGURING_ENDED
)


def follow_all(scenario: Scenario) -> None:
    for action, comments in scenario.items():
        print(get_starting_text(comments))
        action()
        sleep(_STEP_DELAY_SECONDS)
    print(get_finaling_text(_ON_CONFIGURING_ENDED))
