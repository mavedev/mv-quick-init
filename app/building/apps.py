from enum import Enum
from shutil import copy as shcopy
import os
from .scenario import follow_all
from .constants import (
    Scenario,
    _COMMON_KEEP_FILE,
    _PYTHON_WORK_DIRS,
    _PYTHON_EDITOR_DIR,
    _PYTHON_APP_DIR,
    _PYTHON_EDITOR_CONF_FILE,
    _PYTHON_TEMPLATE_PATH,
    _PYTHON_COMMON_IGNORE_FILE,
    _PYTHON_TEMPLATE_MAIN_FILE,
    _PYTHON_TEMPLATE_CONF_FILE,
    _PYTHON_COMMANDS,
    _ON_SETUP_ENVIRONMENT,
    _ON_SETUP_DIRECTORIES,
    _ON_SETUP_START_FILES
)


class AppType(Enum):
    PYTHON_APP = 1
    JS_APP = 2


class App:
    _SOURCE: str = os.path.dirname(os.path.realpath(__file__))

    def create(self) -> None:
        scenario: Scenario = {
            self._setup_environment: _ON_SETUP_ENVIRONMENT,
            self._setup_directories: _ON_SETUP_DIRECTORIES,
            self._setup_start_files: _ON_SETUP_START_FILES
        }
        follow_all(scenario)

    def _setup_environment(self) -> None:
        raise NotImplementedError()

    def _setup_directories(self) -> None:
        raise NotImplementedError()

    def _setup_start_files(self) -> None:
        raise NotImplementedError()


class PythonApp(App):
    def _setup_environment(self) -> None:
        for command in _PYTHON_COMMANDS:
            os.system(command)

    def _setup_directories(self) -> None:
        for folder_ in _PYTHON_WORK_DIRS:
            os.mkdir(folder_)

        open(os.path.join(_PYTHON_APP_DIR, _COMMON_KEEP_FILE), 'w+').close()

    def _setup_start_files(self) -> None:
        source: str = os.path.abspath(
            os.path.join(self._SOURCE, _PYTHON_TEMPLATE_PATH)
        )
        target: str = os.getcwd()
        shcopy(
            os.path.join(source, _PYTHON_COMMON_IGNORE_FILE),
            target
        )
        shcopy(
            os.path.join(source, _PYTHON_TEMPLATE_MAIN_FILE),
            target
        )
        shcopy(
            os.path.join(source, _PYTHON_TEMPLATE_CONF_FILE),
            os.path.join(target, _PYTHON_EDITOR_DIR, _PYTHON_EDITOR_CONF_FILE)
        )


class JSApp(App):
    def _setup_environment(self) -> None:
        pass
