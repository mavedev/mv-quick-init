from .constants import (
    Path,
    JSONConfig,
    _JSON_INDENT_LEVELS
)
import json


def add_to_json(add_to: JSONConfig, add_what: JSONConfig) -> None:
    for key, value in add_what.items():
        add_to[key] = value


def get_json(get_from: Path) -> JSONConfig:
    with open(get_from) as file:
        return json.loads(file.read())


def write_json(write_to: Path, write_what: JSONConfig) -> None:
    with open(write_to, 'w') as outfile:
        json.dump(write_what, outfile, indent=_JSON_INDENT_LEVELS)
