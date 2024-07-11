"""
This module is for ad-hoc tasks not related to the actual working app.
Usage:
    python main.py display_environment_variables
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import json
import os
import sys
import time
import logging
import traceback

from docopt import docopt
from dotenv import load_dotenv

def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version="1.0.0")
    print(arguments)

def display_environment_variables():
    values = dict()
    for name, value in os.environ.items():
        values[name] = value

    for name in sorted(values.keys()):
        display = True
        if name.startswith("CAIG"):
            display = True
        elif name.startswith("GREMLIN"):
            display = True
        if display:
            value = values[name]
            logging.info("{} -> {}".format(name, value))


if __name__ == "__main__":
    # standard initialization of env and logger
    load_dotenv(override=True)
    logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
    if len(sys.argv) < 2:
        print_options("Error: invalid command-line")
        exit(1)
    else:
        try:
            func = sys.argv[1].lower()
            if func == "display_environment_variables":
                display_environment_variables()
            else:
                print_options("Error: invalid function: {}".format(func))
        except Exception as e:
            logging.info(str(e))
            logging.info(traceback.format_exc())
