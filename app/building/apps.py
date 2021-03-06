from enum import Enum
from shutil import copy as shcopy
import os
from .scenario import follow_all
from .json_work import (
    get_json,
    add_to_json,
    write_json
)
from .constants import (
    Scenario,
    Path,
    JSONConfig,
    _COMMON_KEEP_FILE,
    _COMMON_IGNORE_FILE,
    _PYTHON_WORK_DIRS,
    _PYTHON_EDITOR_DIR,
    _PYTHON_APP_DIR,
    _PYTHON_EDITOR_CONF_FILE,
    _PYTHON_TEMPLATE_PATH,
    _PYTHON_TEMPLATE_CONF_FILE,
    _PYTHON_COMMANDS,
    _PYTHON_START_FILES,
    _VANILLAJS_TEMPLATE_PATH,
    _VANILLAJS_PROJECT_JSON,
    _VANILLAJS_PROJECT_JSON_INSERTION,
    _VANILLAJS_COMMANDS,
    _VANILLAJS_WORK_DIRS,
    _VANILLAJS_EDITOR_FILES,
    _VANILLAJS_START_FILES,
    _TYPESCRIPT_TEMPLATE_PATH,
    _TYPESCRIPT_PROJECT_JSON,
    _TYPESCRIPT_PROJECT_JSON_INSERTION,
    _TYPESCRIPT_COMMANDS,
    _TYPESCRIPT_PUBLIC_DIR,
    _TYPESCRIPT_SOURCE_DIR,
    _TYPESCRIPT_TESTER_DIR,
    _TYPESCRIPT_WORK_DIRS,
    _TYPESCRIPT_EDITOR_FILES,
    _TYPESCRIPT_TEMPLATE_MAIN_FILE,
    _ON_SETUP_ENVIRONMENT,
    _ON_SETUP_DIRECTORIES,
    _ON_SETUP_START_FILES
)


class AppType(Enum):
    PYTHON_APP = 1
    JS_APP = 2
    TS_APP = 3


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
    def __init__(self) -> None:
        self.__source: Path = os.path.abspath(
            os.path.join(self._SOURCE, _PYTHON_TEMPLATE_PATH)
        )
        self.__target: Path = os.getcwd()

    def _setup_environment(self) -> None:
        for command in _PYTHON_COMMANDS:
            os.system(command)

    def _setup_directories(self) -> None:
        for folder_ in _PYTHON_WORK_DIRS:
            os.mkdir(folder_)

        open(os.path.join(_PYTHON_APP_DIR, _COMMON_KEEP_FILE), 'w+').close()

    def _setup_start_files(self) -> None:
        for file in _PYTHON_START_FILES:
            shcopy(
                os.path.join(self.__source, file),
                self.__target
            )
        shcopy(
            os.path.join(self.__source, _PYTHON_TEMPLATE_CONF_FILE),
            os.path.join(
                self.__target, _PYTHON_EDITOR_DIR,
                _PYTHON_EDITOR_CONF_FILE
            )
        )


class JSApp(App):
    def __init__(self) -> None:
        self.__source: Path = os.path.abspath(
            os.path.join(self._SOURCE, _VANILLAJS_TEMPLATE_PATH)
        )
        self.__target: Path = os.getcwd()

    def _setup_environment(self) -> None:
        self.__create_json()
        self.__config_json()
        self.__config_libs()

    def _setup_directories(self) -> None:
        for folder_ in _VANILLAJS_WORK_DIRS:
            os.mkdir(folder_)
            open(os.path.join(folder_, _COMMON_KEEP_FILE), 'w+').close()

    def _setup_start_files(self) -> None:
        for file in _VANILLAJS_EDITOR_FILES:
            shcopy(
                os.path.join(self.__source, file),
                self.__target
            )
        for file in _VANILLAJS_START_FILES:
            shcopy(
                os.path.join(self.__source, file),
                self.__target
            )

    def __create_json(self) -> None:
        shcopy(
            os.path.join(self.__source, _VANILLAJS_PROJECT_JSON),
            self.__target
        )

    def __config_json(self) -> None:
        conf_json: JSONConfig = get_json(
            os.path.abspath(_VANILLAJS_PROJECT_JSON)
        )
        insertion: JSONConfig = _VANILLAJS_PROJECT_JSON_INSERTION
        add_to_json(conf_json, insertion)
        write_json(
            os.path.abspath(_VANILLAJS_PROJECT_JSON),
            conf_json
        )

    def __config_libs(self) -> None:
        for command in _VANILLAJS_COMMANDS:
            os.system(command)


class TSApp(App):
    def __init__(self) -> None:
        self.__source: Path = os.path.abspath(
            os.path.join(self._SOURCE, _TYPESCRIPT_TEMPLATE_PATH)
        )
        self.__target: Path = os.getcwd()

    def _setup_environment(self) -> None:
        self.__create_json()
        self.__config_json()
        self.__config_libs()

    def _setup_directories(self) -> None:
        for folder_ in _TYPESCRIPT_WORK_DIRS:
            os.mkdir(folder_)

        open(
            os.path.join(_TYPESCRIPT_PUBLIC_DIR, _COMMON_KEEP_FILE), 'w+'
        ).close()
        open(
            os.path.join(_TYPESCRIPT_TESTER_DIR, _COMMON_KEEP_FILE), 'w+'
        ).close()

    def _setup_start_files(self) -> None:
        for file in _TYPESCRIPT_EDITOR_FILES:
            shcopy(
                os.path.join(self.__source, file),
                self.__target
            )
        shcopy(
            os.path.join(self.__source, _COMMON_IGNORE_FILE),
            self.__target
        )
        shcopy(
            os.path.join(self.__source, _TYPESCRIPT_TEMPLATE_MAIN_FILE),
            os.path.join(self.__target, _TYPESCRIPT_SOURCE_DIR)
        )

    def __create_json(self) -> None:
        shcopy(
            os.path.join(self.__source, _TYPESCRIPT_PROJECT_JSON),
            self.__target
        )

    def __config_json(self) -> None:
        conf_json: JSONConfig = get_json(
            os.path.abspath(_TYPESCRIPT_PROJECT_JSON)
        )
        insertion: JSONConfig = _TYPESCRIPT_PROJECT_JSON_INSERTION
        add_to_json(conf_json, insertion)
        write_json(
            os.path.abspath(_TYPESCRIPT_PROJECT_JSON),
            conf_json
        )

    def __config_libs(self) -> None:
        for command in _TYPESCRIPT_COMMANDS:
            os.system(command)
