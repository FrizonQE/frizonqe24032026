import json
from pathlib import Path

import requests


PDF_URL = "https://github.com/progit/progit2/releases/download/2.1.449/progit.pdf"
ASTROS_URL = "http://api.open-notify.org/astros.json"

PDF_FILE_NAME = "progit.pdf"
JSON_FILE_NAME = "astros.json"


def download_pdf(url: str = PDF_URL, file_name: str = PDF_FILE_NAME) -> None:
    response = requests.get(url)

    if response.status_code == 200:
        Path(file_name).write_bytes(response.content)
        print(f"PDF файл успішно збережено: {file_name}")
    else:
        print(f"Помилка завантаження PDF. Код: {response.status_code}")


def save_json_from_api(url: str = ASTROS_URL, file_name: str = JSON_FILE_NAME) -> None:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"JSON файл успішно збережено: {file_name}")
    else:
        print(f"Помилка отримання JSON. Код: {response.status_code}")


def main() -> None:
    download_pdf()
    save_json_from_api()


if __name__ == "__main__":
    main()