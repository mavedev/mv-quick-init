from typing import List, Dict, Union, Callable
import os

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
_PYTHON_EDITOR_DIR: str = '.vscode'
_PYTHON_APP_DIR: str = 'app'
_PYTHON_WORK_DIRS: List[str] = [
    _PYTHON_EDITOR_DIR,
    _PYTHON_APP_DIR
]
_PYTHON_COMMAND_VENV: str = 'virtualenv venv'
_PYTHON_COMMANDS: List[str] = [
    _PYTHON_COMMAND_VENV,
    _COMMON_COMMAND_GITINIT
]
_PYTHON_TEMPLATE_CONF_FILE: str = 'default.json'
_PYTHON_TEMPLATE_MAIN_FILE: str = '__main__.py'
_PYTHON_START_FILES: List[str] = [
    _PYTHON_TEMPLATE_MAIN_FILE,
    _COMMON_IGNORE_FILE
]
_PYTHON_EDITOR_CONF_FILE: str = 'settings.json'
_PYTHON_TEMPLATE_PATH: str = '../../templates/python'

# VanillaJS config.
_VANILLAJS_TEMPLATE_PATH: Path = '../../templates/vanillajs'
_VANILLAJS_PROJECT_JSON: str = 'package.json'
_VANILLAJS_PROJECT_JSON_INSERTION: JSONConfig = {
    'name': os.path.basename(os.getcwd())
}
_VANILLAJS_ESLINT_COMMAND: str = 'npm i -D eslint@5'
_VANILLAJS_AIRBNB_COMMAND: str = 'npm i -D eslint-config-airbnb-base'
_VANILLAJS_PLUGIN_COMMAND: str = 'npm i -D eslint-plugin-import@^2.20.1'
_VANILLAJS_COMMANDS: List[str] = [
    _VANILLAJS_ESLINT_COMMAND,
    _VANILLAJS_AIRBNB_COMMAND,
    _VANILLAJS_PLUGIN_COMMAND,
    _COMMON_COMMAND_GITINIT
]
_VANILLAJS_PUBLIC_DIR: str = 'public'
_VANILLAJS_TESTER_DIR: str = 'test'
_VANILLAJS_WORK_DIRS = [
    _VANILLAJS_PUBLIC_DIR,
    _VANILLAJS_TESTER_DIR
]
_VANILLAJS_EDITOR_FILES: List[str] = [
    '.editorconfig',
    '.eslintrc.json',
    '.eslintignore',
]
_VANILLAJS_TEMPLATE_MAIN_FILE: str = 'index.js'
_VANILLAJS_START_FILES: List[str] = [
    _VANILLAJS_TEMPLATE_MAIN_FILE,
    _COMMON_IGNORE_FILE
]

# Typescript config.
_TYPESCRIPT_TEMPLATE_PATH: Path = '../../templates/typescript'
_TYPESCRIPT_PROJECT_JSON: str = 'package.json'
_TYPESCRIPT_PROJECT_JSON_INSERTION: JSONConfig = {
    'name': os.path.basename(os.getcwd())
}
_TYPESCRIPT_ESLINT_COMMAND: str = 'npm i -D eslint@5'
_TYPESCRIPT_PARSER_COMMAND: str = 'npm i -D @typescript-eslint/parser'
_TYPESCRIPT_PLUGIN_COMMAND: str = 'npm i -D @typescript-eslint/eslint-plugin'
_TYPESCRIPT_TSCORE_COMMAND: str = 'npm i -D typescript'
_TYPESCRIPT_TYPING_COMMAND: str = 'npm i --save @types/node'
_TYPESCRIPT_COMMANDS: List[str] = [
    _TYPESCRIPT_ESLINT_COMMAND,
    _TYPESCRIPT_PARSER_COMMAND,
    _TYPESCRIPT_PLUGIN_COMMAND,
    _TYPESCRIPT_TSCORE_COMMAND,
    _TYPESCRIPT_TYPING_COMMAND,
    _COMMON_COMMAND_GITINIT
]
_TYPESCRIPT_PUBLIC_DIR: str = 'dist'
_TYPESCRIPT_SOURCE_DIR: str = 'src'
_TYPESCRIPT_TESTER_DIR: str = 'test'
_TYPESCRIPT_WORK_DIRS = [
    _TYPESCRIPT_PUBLIC_DIR,
    _TYPESCRIPT_SOURCE_DIR,
    _TYPESCRIPT_TESTER_DIR
]
_TYPESCRIPT_EDITOR_FILES: List[str] = [
    '.editorconfig',
    '.eslintrc.json',
    '.eslintignore',
    'tsconfig.json'
]
_TYPESCRIPT_TEMPLATE_MAIN_FILE: str = 'index.ts'
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
