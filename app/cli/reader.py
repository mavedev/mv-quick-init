import argparse
import sys


def get_parsed_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        conflict_handler='resolve',
        description='Starts a Python or JS project.',
        epilog='https://github.org/mavedev/mv-quick-init'
    )
    parser.add_argument(
        '--py',
        action='store_true',
        help='Init a Python project and configure the virtual environment.'
    )
    parser.add_argument(
        '--js',
        action='store_true',
        help='Init a Javascript project.'
    )
    if not sys.argv[1:]:
        parser.print_help()

    return parser.parse_args()
