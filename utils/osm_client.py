import requests
from requests.exceptions import RequestException
from utils.config import load_config

def fetch_osm_data(query):
    request_timeout = load_config()["request_timeout"]

    headers = {
        "User-Agent": "LeadFinder/1.0",
        "Referer": "https://www.openstreetmap.org/"
    }

    try:
        response = requests.post(
            "https://maps.mail.ru/osm/tools/overpass/api/interpreter",
            data=query,
            headers=headers,
            timeout=request_timeout
        )

    except RequestException as error:
        print(f"Первая попытка не удалась: {error}")
        print("Повторяю запрос...")

        try:
            response = requests.post(
                "https://maps.mail.ru/osm/tools/overpass/api/interpreter",
                data=query,
                headers=headers,
                timeout=request_timeout
            )

        except RequestException as error:
            print(f"Ошибка запроса после повторной попытки: {error}")
            return


    if response.status_code != 200:
        print(response.text)
        return
    return response