import requests

import logging
import time

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")


def get_server_players_count(server_ip):
    start_time = time.time()

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "PostmanRuntime/7.40.0",
        "Accept": "*/*",
    }

    request = requests.request("GET", f"https://api.mcstatus.io/v2/status/java/{server_ip}", headers=headers)

    try:
        src = request.json()
        logging.info(f"Время запроса: {time.time() - start_time}")

        if "players" in src:
            return src['players']  # передаем инфу об игроках сервера
        else:
            return None  # если юзер ввел ссылку на обычный сайт, а не сервер

    except requests.exceptions.JSONDecodeError:
        return None  # если юзер ввел не ссылку


if __name__ == "__main__":
    print(get_server_players_count("miranda.minerent.net:25582"))
    print(get_server_players_count("zzzzz"))
