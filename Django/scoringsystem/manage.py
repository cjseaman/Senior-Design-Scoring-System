# File: manage.py
# Description: This file holds Django's command-line utility for
#   administrative tasks.

#!/usr/bin/env python
import os
import sys

# Function name: main
# Parameters: None
# Returns: None
# Description: Sets up the environment for Django, and raises an error
#   if it is not installed/invoked correctly.
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scoringsystem.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
