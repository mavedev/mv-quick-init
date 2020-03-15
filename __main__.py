# -*- coding: utf-8 -*-
from app.cli.reader import get_parsed_arguments
from argparse import Namespace

from app.building import AppFactory, AppType


def main() -> None:
    args: Namespace = get_parsed_arguments()
    if args.py:
        AppFactory.get_app(AppType.PYTHON_APP).create()
    elif args.js:
        AppFactory.get_app(AppType.JS_APP).create()


if __name__ == '__main__':
    main()
