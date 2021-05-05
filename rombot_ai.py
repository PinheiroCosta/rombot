from rombot_commands import bot
import ai_library
import random


def speech_option(choice, enunciated):
  option = {"some": ai_library.soma_lista(enunciated),
            "liste": enunciated,
            "diga": " ".join(enunciated),
            "enquete": ai_library.enquete(enunciated)
            }

  return option[choice]


class Ai:
  @bot.event
  async def on_message(message):
    await bot.process_commands(message)
    autor = message.author
    msg = message.content

    if message.author == bot.user:
      if msg.split()[0] == "Enquete:":
        await message.add_reaction('\N{THUMBS UP SIGN}')
        await message.add_reaction('\N{THUMBS DOWN SIGN}')
      return

    # retorna mensagem caso seja mencionado
    if str(bot.user.id) in msg:
      greeting = ["Oi", "Olá", "Falae" ]
      ordem = msg.split()[1]
      enunciado = msg.split()[2:]
      hello = f"{random.choice(greeting)} {autor.name}, Como posso te ajudar? Converse comigo na forma imperativa, ou digite {bot.command_prefix}help para saber quais comandos posso executar"
      
      try:
        await message.channel.send(speech_option(ordem, enunciado))

      except IndexError:
        await message.channel.send(hello)
      
      except KeyError:
        await message.channel.send(hello)
