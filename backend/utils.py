import logging
from functools import wraps

logging.basicConfig(filename="logs.csv", level=logging.INFO, format="%(asctime)s,%(message)s")

def log_action(action):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(action)
            return func(*args, **kwargs)
        return wrapper
    return decorator
