import os
import discord
from rombot_commands import bot
from rombot_ai import Ai


intents = discord.Intents.default()
intents.members = True

speech = Ai()


@bot.event
async def on_ready():
    print(f"logado como {bot.user}")


bot.run(os.getenv('TOKEN'))
