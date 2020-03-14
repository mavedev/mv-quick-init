from .apps import (
    AppType, App, PythonApp, JSApp
)


class AppFactory:
    @classmethod
    def get_app(cls, app_type: AppType) -> App:
        return {
            AppType.PYTHON_APP: PythonApp(),
            AppType.JS_APP: JSApp()
        }[app_type]
