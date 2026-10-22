import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()

    request_timeout = os.getenv("REQUEST_TIMEOUT", "30")
    max_workers = os.getenv("MAX_WORKERS", "20")

    request_timeout = int(request_timeout)
    max_workers = int(max_workers)

    if request_timeout <=0:
        raise ValueError("Должен быть больше 0")

    if max_workers <=0:
        raise ValueError("Должен быть больше 0")
    return {
        "request_timeout": request_timeout,
        "max_workers": max_workers,
    }


