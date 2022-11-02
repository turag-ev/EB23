import logging
import inspect
import os
from pathlib import Path

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0


def get_logger(level=logging.INFO, path="Main/logs/"):
    """returns a logger instance which logs to console and to file.
    Logs always with DEBUG Level to file and by default with INFO Level to console (changeable)
    For use in other modules import and call get_logger which returns a logger instance which can be used to log via .debug(), .info(), .warn(), .error()

    Might need to use 'sys.path.insert(0, "./Main")' before importinh if other module is not on a higher level than this module (most of the cases)
    --> this assumes that you are starting every module from git base folder (eurobot2022)

    Args:
        level (logging.Level, optional): Specifies Logging level of console logger. Defaults to logging.INFO.
        path (str, optional): path where log files are saved. Defaults to "Main/Logger/logs/".

    Returns:
        logging.Logger: logger instance
    """
    if not os.path.isdir(path):
        while True:
            print(
                f"Directory 'logs' for storing log files does not exist, should it be created at {os.path.abspath(path)}?"
            )
            valid = {"yes": True, "y": True, "no": False, "n": False}
            print("[y/n or yes/no]")
            choice = input().lower()
            if choice in valid:
                if valid[choice]:
                    Path(path).mkdir(parents=True, exist_ok=True)
                    break
                else:
                    print("using path where file is executed from")
                    path = ""
                    break
            else:
                print("Please respond with 'yes' or 'no' " "(or 'y' or 'n')")

    frm = inspect.stack()[1]
    name = inspect.getmodule(frm[0]).__name__
    formatter = logging.Formatter(
        fmt="%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    file = logging.FileHandler(path + name + ".log", mode="a")
    file.setFormatter(formatter)
    file.setLevel(logging.DEBUG)
    logger.addHandler(file)

    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger
