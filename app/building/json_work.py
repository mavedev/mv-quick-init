from typing import Dict, Union
import json


JSON = Dict[str, str]
Path = Union[str]


def add_to_json(add_to: JSON, add_what: JSON) -> None:
    for key, value in add_what.items():
        add_to[key] = value


def get_json(get_from: Path) -> JSON:
    with open(get_from) as file:
        return json.loads(file.read())


def write_json(write_to: Path, write_what: JSON) -> None:
    with open(write_to, 'w') as outfile:
        json.dump(write_what, outfile)
