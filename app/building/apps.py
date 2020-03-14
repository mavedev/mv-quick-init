from enum import Enum


class AppType(Enum):
    PYTHON_APP = 1
    JS_APP = 2


class App:
    def create(self) -> None:
        raise NotImplementedError()


class PythonApp(App):
    def create(self) -> None:
        pass


class JSApp(App):
    def create(self) -> None:
        pass
