from typing import List, Dict, Callable

from app.cli import get_finaling_text
from .scenario import follow_all

from enum import Enum
from shutil import copy as shcopy
import time
import os


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
        commented_actions: Dict[Callable, str] = {
            self.__setup_venv: 'Generating a virtual '
                               'environment for the project...',
            self.__create_work_dirs: 'Creating a config directory.',
            self.__copy_templates: 'Configuring default user '
                                   'linting settings...'
        }

        follow_all(commented_actions)
        time.sleep(2)
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
