from typing import List, Dict, Union, Callable

# Types.
Comments = Union[str]
Scenario = Dict[Callable, Comments]

# Python config.
_PYTHON_WORK_DIRS: List[str] = [
    '.vscode',
    'app'
]
_PYTHON_EDITOR_DIR: str = '.vscode'
_PYTHON_EDITOR_CONF_FILE: str = 'settings.json'
_PYTHON_TEMPLATE_PATH: str = '../../templates/python'
_PYTHON_TEMPLATE_CONF_FILE: str = 'default.json'
_PYTHON_TEMPLATE_MAIN_FILE: str = '__main__.py'

# Commands.
_VENV_COMMAND: str = 'virtualenv venv'

# Ouptut.
_ON_SETUP_ENVIRONMENT: str = 'Configuring environment for the project...'
_ON_SETUP_DIRECTORIES: str = 'Configuring directories for the project...'
_ON_SETUP_START_FILES: str = 'Configuring start files for the project...'
_ON_CONFIGURING_ENDED: str = 'Done.'

# Numbers.
_STEP_DELAY_SECONDS: int = 1
