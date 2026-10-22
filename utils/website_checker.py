import requests
from concurrent.futures import ThreadPoolExecutor
from utils.config import load_config

def check_website(url):

    if url is None:
        return False

    try:
        response = requests.get(
            url,
            timeout=(2, 3),
            allow_redirects=True
        )
        response.raise_for_status()
        return True

    except requests.exceptions.RequestException:
        return False


def check_websites(urls, max_workers=None):
    if max_workers is None:
        max_workers = load_config()["max_workers"]


    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(check_website, urls)

    return list(results)