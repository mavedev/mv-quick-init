from typing import List, Dict, Union, Callable

# Types.
Comments = Union[str]
Scenario = Dict[Callable, Comments]

# Common config.
_COMMON_KEEP_FILE: str = '.gitkeep'
_COMMON_COMMAND_GITINIT: str = 'git init'

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
_PYTHON_COMMON_IGNORE_FILE: str = '.gitignore'
_PYTHON_TEMPLATE_CONF_FILE: str = 'default.json'
_PYTHON_TEMPLATE_MAIN_FILE: str = '__main__.py'
_PYTHON_EDITOR_CONF_FILE: str = 'settings.json'
_PYTHON_TEMPLATE_PATH: str = '../../templates/python'

# VanillaJS config.


# Ouptut.
_ON_SETUP_ENVIRONMENT: str = 'Configuring environment for the project...'
_ON_SETUP_DIRECTORIES: str = 'Configuring directories for the project...'
_ON_SETUP_START_FILES: str = 'Configuring start files for the project...'
_ON_CONFIGURING_ENDED: str = 'Done.'

# Numbers.
_STEP_DELAY_SECONDS: int = 1
