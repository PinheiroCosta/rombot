from rombot_commands import bot
import random


class Ai:
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
      greeting = ["Oi", "Olá", "Falae" ]
      
      if any(word in msg for word in help):
        await message.channel.send(f"{random.choice(greeting)} {autor.name},",
                                        "Como posso te ajudar? Converse comigo na forma imperativa,",
                                        "ou digite {bot.command_prefix}help para saber quais comandos posso executar")
        
      else:
        await message.channel.send(f"Opa! Alguém aí me chamou?")
