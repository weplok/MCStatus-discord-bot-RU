# MCStatus-discord-bot-RU

Простой discord-бот, позволяющий следить за количеством игроков на любом сервере Minecraft.

***

### [Как запустить](#how-run)

### [Команды бота](#commands)

### [Галерея](#gallery)

***

<a name="how-run"></a>

## Как запустить

Создайте [приложение Discord](https://discord.com/developers/applications), сохраните себе его _APPLICATION ID_ (_CLIENT ID_)

Настройте бота на вкладке Bots. Обязательно включите _PRESENCE INTENT_, _SERVER MEMBERS INTENT_, _MESSAGE CONTENT INTENT_

На вкладке _Bots_ возьмите _TOKEN_ своего бота, вставьте этот токен в файл _example.env_

Вы можете заменить IP по умолчанию в _example.env_

Переименуйте "_example.env_" в "_.env_"

Добавьте бота на Ваш сервер с помощью ссылки, в которую вставьте _CLIENT-ID_ своего приложения:

```site
https://discord.com/oauth2/authorize?client_id=CLIENT-ID&permissions=2147552256
```

Скачайте нужные зависимости:

```commandline
pip install -r requirements.txt
```

Запустите бота:

```commandline
python bot.py
```

***

<a name="commands"></a>

## Команды бота

* **/players {server-ip}** — Узнать онлайн конкретного сервера
* **/players** — Узнать онлайн сервера по умолчанию (из .env файла)

***

<a name="gallery"></a>

## Галерея

![Пример 1](https://i.imgur.com/PiggZzk.png)

![Пример 2](https://i.imgur.com/ERHscbS.png)
