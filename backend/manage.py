#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path
import configparser


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'management.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if sys.argv[1] == "runserver":
        BASE_DIR = Path(__file__).resolve().parent
        if not os.path.isfile(os.path.join(BASE_DIR, 'config.ini')):
            print("Please create config.ini first")
            exit(1)
        CONFIG = configparser.RawConfigParser()
        CONFIG.read(os.path.join(BASE_DIR, 'config.ini'))
        if 'DJANGO' not in CONFIG:
            exit(1)
        if not CONFIG.get('DJANGO', 'MANUAL_MIGRATE', fallback=False):
            execute_from_command_line(['manage.py', 'migrate'])
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
