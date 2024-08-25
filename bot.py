import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

from main import get_server_players_count

load_dotenv()
TOKEN = os.getenv("TOKEN")
DEFAULT_IP = os.getenv("DEFAULT_IP")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'Бот {bot.user} готов к использованию (ID: {bot.user.id})')
    print('------')


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def players(ctx, arg=DEFAULT_IP):  # аргумент - ip сервера
    data = get_server_players_count(arg)  # получаем информацию об игроках сервера
    if data is None:
        ans = "Не удалось найти сервер"
    else:
        ans = f"Количество игроков на сервере __{arg}__:\n* *{data['online']} / {data['max']}*"
        if len(data['list']) != 0:
            players_list = [player['name_clean'] for player in data['list'][:10]]
            players_list_str = '\n* '.join(players_list)
            if len(data['list']) > 10:
                ans += f"\nПервые 10 игроков на сервере:\n>>> * {players_list_str}"
            else:
                ans += f"\nИгроки на сервере:\n>>> * {players_list_str}"

    await ctx.send(ans)  # отправляем ответ пользователю


bot.run(TOKEN)
