import csv
from functools import wraps
from datetime import datetime
from .config import LOGS_CSV

def log_action(operation):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(LOGS_CSV, "a", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                if f.tell() == 0:
                    writer.writerow(["timestamp", "operation", "details"])
                writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), operation, str(kwargs)])
            return result
        return wrapper
    return decorator
