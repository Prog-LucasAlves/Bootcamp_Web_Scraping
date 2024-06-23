import requests
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv("api")


def jogos():
    url = f"{URL}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }

    content = requests.get(url, headers=headers)

    return print(content)


if __name__ == "__main__":
    jogos()
