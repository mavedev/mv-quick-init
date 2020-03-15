from typing import Dict, Callable

from app.cli import get_finaling_text
from .scenario import follow_all
from .constants import (
    _PYTHON_WORK_DIRS,
    _PYTHON_EDITOR_DIR,
    _PYTHON_EDITOR_CONF_FILE,
    _PYTHON_TEMPLATE_PATH,
    _PYTHON_TEMPLATE_MAIN_FILE,
    _PYTHON_TEMPLATE_CONF_FILE,
    _VENV_COMMAND
)

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
        os.system(_VENV_COMMAND)

    def __create_work_dirs(self) -> None:
        for dir_ in _PYTHON_WORK_DIRS:
            os.mkdir(dir_)

    def __copy_templates(self) -> None:
        source: str = os.path.abspath(
            os.path.join(self._SOURCE, _PYTHON_TEMPLATE_PATH)
        )
        target: str = os.getcwd()
        shcopy(
            os.path.join(source, _PYTHON_TEMPLATE_MAIN_FILE),
            target
        )
        shcopy(
            os.path.join(source, _PYTHON_TEMPLATE_CONF_FILE),
            os.path.join(target, _PYTHON_EDITOR_DIR, _PYTHON_EDITOR_CONF_FILE)
        )


class JSApp(App):
    def create(self) -> None:
        pass
