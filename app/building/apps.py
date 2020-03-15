from app.cli import get_starting_text, get_finaling_text

from enum import Enum
from shutil import copy as shcopy
import time
import os

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import List


class AppType(Enum):
    PYTHON_APP = 1
    JS_APP = 2


class App:
    _SOURCE: str = os.path.dirname(os.path.realpath(__file__))

    def create(self) -> None:
        raise NotImplementedError()


class PythonApp(App):
    _WORK_DIRS_PYTHON: List[str] = [
        '.vscode',
        'app'
    ]

    def create(self) -> None:
        print(get_starting_text(
            'Generating a virtual environment for the project...'
        ))
        self.__setup_venv()

        print(get_starting_text(
            'Creating a config directory.'
        ))
        self.__create_work_dirs()

        print(get_starting_text(
            'Configuring default user linting settings...'
        ))
        self.__copy_templates()

        print(get_finaling_text(
            'Done.'
        ))

    def __setup_venv(self) -> None:
        os.system('virtualenv venv')

    def __create_work_dirs(self) -> None:
        for dir_ in self._WORK_DIRS_PYTHON:
            os.mkdir(dir_)

    def __copy_templates(self) -> None:
        source: str = os.path.abspath(
            os.path.join(self._SOURCE, '../../templates/python')
        )
        target: str = os.getcwd()
        for file_name in os.listdir(source):
            full_file_name = os.path.join(source, file_name)
            shcopy(full_file_name, target)


class JSApp(App):
    def create(self) -> None:
        pass
