import os
import discord
from discord.ext import commands
from time import sleep


help_command = commands.DefaultHelpCommand(
    no_category = 'Commandos')

bot = commands.Bot(
  command_prefix='?',
  description="Os comandos devem ser precedidos pelo caractere '?' e alguns deles aceitam [parâmetros] - sem chaves - opcionais. Desenvolvido por Rômulo - https://github.com/PinheiroCosta",
  help_command=help_command)

intents = discord.Intents.default()
intents.members = True


@bot.event
async def on_ready():
  print(f"logado como {bot.user}")

@bot.event
async def on_message(message):
  await bot.process_commands(message)
  autor = message.author
  msg = message.content

  if message.author == bot.user:
    return

  # retorna mensagem caso seja mencionado
  if str(bot.user.id) in msg:
    help = ["ajuda", "ajudar", "socorro", "ajude"]
    if any(word in msg for word in help):
      await message.channel.send(f"Olá {autor.name}, Como posso ajudar? Digite {bot.command_prefix}help para saber quais comandos posso executar")
    else:
      await message.channel.send(f"Opa! Alguém me chamou?")


@bot.command()
async def id(ctx, member: discord.Member):
  """[@membro] Diz o ID de uma pessoa"""

  await ctx.channel.send(f"O id de {member} é: {member.id}")

@bot.command()
async def get_status(ctx, member: discord.Member):
  """[@membro] Diz o que a pessoa está fazendo"""

  game = member.activities[0]
  await ctx.channel.send(f"{member.name} está jogando {game}")

@bot.command()
async def bot_gameplay(ctx, *, act):
  """[nome do jogo] Muda a atividade do bot"""

  await bot.change_presence(activity=discord.Game(name=act))
  
@bot.command()
async def ch_transfer(ctx, member: discord.Member, channel: discord.VoiceChannel, reason=None):
  """[@membro] [canal] Transfere a pessoa para outro canal"""

  await member.move_to(channel, reason=None)
  await ctx.channel.send(f"{member} foi para o canal {channel}")

@bot.command()
async def cls(ctx, limit=100):
  """[número](opcional) Limpa mensagens do canal atual"""

  await ctx.channel.send(f"Deletando mensagens do canal {ctx.channel}...")
  sleep(3)
  await ctx.channel.purge(limit=limit)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="eu quis"):
  """[@membro] [motivo](opcional) chuta pessoa do servidor"""

  if member.id == "264822085623349248":
    await ctx.channel.send("O quêêêêê? você quer que eu expulse meu próprio criador daqui?\n https://tenor.com/3vIV.gif")
  else:
    await member.kick(reason=reason)
    await ctx.channel.send(f"{member} não está mais no servidor porque {reason}")

@kick.error
async def info_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
      await ctx.channel.send(f"Não foi possível expulsar essa pessoa. Não temos permissão para isso")

@bot.command()
@commands.has_permissions(manage_nicknames=True)
async def nick_edit(ctx, member: discord.Member, nick):
  """[@membro] [Apelido] Altera o apelido da pessoa"""

  await member.edit(reason=None, nick=nick)
  await ctx.channel.send(f"O nick de {member.name} foi alterado para {nick}")

@nick_edit.error
async def info_error(ctx, error):
  if isinstance(error, commands.CommandInvokeError):
    await ctx.channel.send(f"Não foi possível mudar o nick dessa pessoa. Não temos permissão para isso.")

@bot.command()
async def mute(ctx, member: discord.Member):
  """[@membro] Silencia a pessoa"""

  await member.edit(reason=None, mute=1)
  await ctx.channel.send(f"{member.name} foi silenciado(a)")


@bot.command()
async def unmute(ctx, member: discord.Member):
  """[@membro] devolve a voz da pessoa"""

  await member.edit(reason=None, mute=0)
  await ctx.channel.send(f"{member.name} já pode falar novamente")


bot.run(os.getenv('TOKEN'))
