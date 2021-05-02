import discord
import os


client = discord.Client()

@client.event
async def on_ready():
  print(f"Logado como {client.user}")


@client.event
async def on_message(message):
  autor = message.author
  if message.author == client.user:
    return

  if message.content == "%hello":
    await message.channel.send(f"Olá {autor.name}!")

client.run(os.getenv('TOKEN'))
