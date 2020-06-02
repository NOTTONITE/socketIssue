from threading import Thread
from discord.ext import commands
import socketListener

bot = commands.Bot(command_prefix='tb:')
with open("token.txt") as f: token = f.readline()


@bot.event
async def on_ready():
    print('ready')


Thread(target=socketListener.run).start()
bot.run(token)
