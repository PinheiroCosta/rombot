from discord.ext import commands
from time import sleep
import discord
import os


help_command = commands.DefaultHelpCommand(
    no_category = 'Commandos')

bot = commands.Bot(
  command_prefix='>',
  description=f"Os comandos devem ser precedidos pelo caractere '>'. Os [parâmetros] que possuírem um asterístico são obrigatórios.",
  help_command=help_command)

# Comandos de Informação
@bot.command()
async def id(ctx, member: discord.Member):
  """[@membro]* Diz o ID de uma pessoa"""
  await ctx.channel.send(f"O id de {member} é: {member.id}")

@bot.command()
async def get_status(ctx, member: discord.Member):
  """[@membro]* Diz o que a pessoa está fazendo"""
  game = member.activities
  await ctx.channel.send(f"{member.name} está jogando {game}")

@bot.command()
async def bot_gameplay(ctx, *, act):
  """[nome do jogo]* Muda a atividade do bot"""
  await bot.change_presence(activity=discord.Game(name=act))  
  
# Comandos de Gerenciamento  
@bot.command()
async def ch_transfer(ctx, member: discord.Member, channel: discord.VoiceChannel, reason=None):
  """[@membro]* [canal]* Transfere a pessoa para outro canal"""
  await member.move_to(channel, reason=None)
  await ctx.channel.send(f"{member} foi para o canal {channel}")

@bot.command(name='clear', aliases=['Clear'])
async def clear(ctx, limit=100):
  """[número]* Limpa mensagens do bot do canal atual"""
  await ctx.channel.send(f"Deletando minhas mensagens do canal {ctx.channel.mention} ...")
  sleep(2)
  if_not_pinned_and_bot = lambda msg: not msg.pinned and msg.author == bot.user
  deleted = await ctx.channel.purge(limit=limit, check=if_not_pinned_and_bot)  
  await ctx.channel.send(f"{len(deleted)} mensagens foram excluídas", delete_after=3)

@bot.command(name='purge', aliases=['Purge'])
async def clear_all(ctx, limit=100):
  """[número]* Limpa mensagens do canal atual"""
  await ctx.channel.send(f"Deletando mensagens do canal {ctx.channel.mention} ...")
  sleep(2)
  if_not_pinned = lambda msg: not msg.pinned
  deleted = await ctx.channel.purge(limit=limit, check=if_not_pinned)  
  await ctx.channel.send(f"{len(deleted)} mensagens foram excluídas", delete_after=3)

@bot.command(name='kick', aliases=['Kick'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="eu quis"):
  """[@membro]* [motivo] chuta pessoa do servidor"""
  await member.kick(reason=reason)
  await ctx.channel.send(f"{member} não está mais no servidor porque {reason}")

@kick.error
async def info_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
      await ctx.channel.send(f"Não foi possível expulsar essa pessoa. Talvez ela esteja numa hierarquia acima de mim?")

@bot.command()
async def nick_edit(ctx, member: discord.Member, nick):
  """[@membro]* [Apelido]* Altera o apelido da pessoa"""
  await member.edit(reason=None, nick=nick)
  await ctx.channel.send(f"O nick de {member.name} foi alterado para {nick}")

@nick_edit.error
async def info_error(ctx, error):
  if isinstance(error, commands.CommandInvokeError):
    await ctx.channel.send(f"Não foi possível mudar o nick dessa pessoa. Não temos permissão para isso.")

@bot.command()
async def mute(ctx, member: discord.Member):
  """[@membro]* Silencia a pessoa"""
  await member.edit(reason=None, mute=1)
  await ctx.channel.send(f"{member.name} foi silenciado(a)")


@bot.command()
async def unmute(ctx, member: discord.Member):
  """[@membro]* devolve a voz da pessoa"""
  await member.edit(reason=None, mute=0)
  await ctx.channel.send(f"{member.name} já pode falar novamente")

@bot.command()
async def clone(ctx, member: discord.Member):
  """[@membro]* Clona o nome de um membro"""
  await ctx.guild.me.edit(nick=member.name) 
  await ctx.channel.send(f"{member.name} foi clonado!")
