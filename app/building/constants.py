from typing import List, Dict, Union, Callable
import os
from configparser import SafeConfigParser

configer = SafeConfigParser()
is_ok = configer.read(
    os.path.abspath(os.path.join(__file__, '../../../settings.conf'))
)

# Types.
Comments = Union[str]
Scenario = Dict[Callable, Comments]
JSONConfig = Dict[str, Union[str, Dict[str, str]]]
Path = Union[str]

# Common config.
_COMMON_KEEP_FILE: str = '.gitkeep'
_COMMON_COMMAND_GITINIT: str = 'git init'
_COMMON_IGNORE_FILE: str = '.gitignore'

# Python config.
_PYTHON_EDITOR_DIR: str = configer.get('editor', 'editor_dir')
_PYTHON_APP_DIR: str = configer.get('python', 'app_dirname')
_PYTHON_WORK_DIRS: List[str] = [
    _PYTHON_EDITOR_DIR,
    _PYTHON_APP_DIR
]
_PYTHON_COMMAND_VENV: str = configer.get('python', 'venv_command')
_PYTHON_COMMANDS: List[str] = [
    _PYTHON_COMMAND_VENV,
    _COMMON_COMMAND_GITINIT
]
_PYTHON_EDITOR_CONF_FILE: str = configer.get('editor', 'python_config_dest')
_PYTHON_TEMPLATE_PATH: Path = configer.get('templates', 'py_template_path')
_PYTHON_TEMPLATE_CONF_FILE: str = configer.get('editor', 'python_config_from')
_PYTHON_TEMPLATE_MAIN_FILE: str = configer.get('python', 'app_entry_filename')
_PYTHON_START_FILES: List[str] = [
    _PYTHON_TEMPLATE_MAIN_FILE,
    _COMMON_IGNORE_FILE
]

# VanillaJS config.
_VANILLAJS_PUBLIC_DIR: str = configer.get('js', 'public_dirname')
_VANILLAJS_TESTER_DIR: str = configer.get('js', 'test_dirname')
_VANILLAJS_WORK_DIRS = [
    _VANILLAJS_PUBLIC_DIR,
    _VANILLAJS_TESTER_DIR
]
_VANILLAJS_ESLINT_COMMAND: str = configer.get('js', 'linter_install_command')
_VANILLAJS_AIRBNB_COMMAND: str = configer.get('js', 'styles_install_command')
_VANILLAJS_PLUGIN_COMMAND: str = configer.get('js', 'plugin_install_command')
_VANILLAJS_COMMANDS: List[str] = [
    _VANILLAJS_ESLINT_COMMAND,
    _VANILLAJS_AIRBNB_COMMAND,
    _VANILLAJS_PLUGIN_COMMAND,
    _COMMON_COMMAND_GITINIT
]
_VANILLAJS_PROJECT_JSON: str = 'package.json'
_VANILLAJS_PROJECT_JSON_INSERTION: JSONConfig = {
    'name': os.path.basename(os.getcwd())
}
_VANILLAJS_EDITOR_FILES: List[str] = [
    '.editorconfig',
    '.eslintrc.json',
    '.eslintignore',
]
_VANILLAJS_TEMPLATE_PATH: Path = configer.get('templates', 'js_template_path')
_VANILLAJS_TEMPLATE_MAIN_FILE: str = configer.get('js', 'app_entry_filename')
_VANILLAJS_START_FILES: List[str] = [
    _VANILLAJS_TEMPLATE_MAIN_FILE,
    _COMMON_IGNORE_FILE
]

# Typescript config.
_TYPESCRIPT_PUBLIC_DIR: str = configer.get('ts', 'dist_dirname')
_TYPESCRIPT_TESTER_DIR: str = configer.get('ts', 'test_dirname')
_TYPESCRIPT_SOURCE_DIR: str = configer.get('ts', 'source_dirname')
_TYPESCRIPT_WORK_DIRS = [
    _TYPESCRIPT_PUBLIC_DIR,
    _TYPESCRIPT_SOURCE_DIR,
    _TYPESCRIPT_TESTER_DIR
]
_TYPESCRIPT_ESLINT_COMMAND: str = configer.get('ts', 'linter_install_command')
_TYPESCRIPT_PARSER_COMMAND: str = configer.get('ts', 'parser_install_command')
_TYPESCRIPT_PLUGIN_COMMAND: str = configer.get('ts', 'plugin_install_command')
_TYPESCRIPT_TSCORE_COMMAND: str = configer.get('ts', 'tscore_install_command')
_TYPESCRIPT_TYPING_COMMAND: str = configer.get('ts', 'typing_install_command')
_TYPESCRIPT_COMMANDS: List[str] = [
    _TYPESCRIPT_ESLINT_COMMAND,
    _TYPESCRIPT_PARSER_COMMAND,
    _TYPESCRIPT_PLUGIN_COMMAND,
    _TYPESCRIPT_TSCORE_COMMAND,
    _TYPESCRIPT_TYPING_COMMAND,
    _COMMON_COMMAND_GITINIT
]
_TYPESCRIPT_PROJECT_JSON: str = 'package.json'
_TYPESCRIPT_PROJECT_JSON_INSERTION: JSONConfig = {
    'name': os.path.basename(os.getcwd())
}
_TYPESCRIPT_EDITOR_FILES: List[str] = [
    '.editorconfig',
    '.eslintrc.json',
    '.eslintignore',
    'tsconfig.json'
]
_TYPESCRIPT_TEMPLATE_PATH: Path = configer.get('templates', 'ts_template_path')
_TYPESCRIPT_TEMPLATE_MAIN_FILE: str = configer.get('ts', 'app_entry_filename')
_TYPESCRIPT_START_FILES: List[str] = [
    _TYPESCRIPT_TEMPLATE_MAIN_FILE,
    _COMMON_IGNORE_FILE
]

# Ouptut.
_ON_SETUP_ENVIRONMENT: str = 'Configuring environment for the project...'
_ON_SETUP_DIRECTORIES: str = 'Configuring directories for the project...'
_ON_SETUP_START_FILES: str = 'Configuring start files for the project...'
_ON_CONFIGURING_ENDED: str = 'Done.'

# Numbers.
_STEP_DELAY_SECONDS: int = 1
_JSON_INDENT_LEVELS: int = 2
