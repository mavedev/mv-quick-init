from .constants import _BColors


def get_starting_text(text: str) -> str:
    return _get_surrounded_text(
        start=f'{_BColors.GREEN}',
        text=text
    )


def get_finaling_text(text: str) -> str:
    return _get_surrounded_text(
        start=f'{_BColors.YELLOW}',
        text=text
    )


def _get_surrounded_text(start: str, text: str) -> str:
    return start + text + f'{_BColors.ENDC}'
