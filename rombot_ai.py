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
      greeting = ["Oi", "Olá", "Falae" ]
      ordem = msg.split()[1]
      enunciado = msg.split()[2:]
      hello = f"{random.choice(greeting)} {autor.name}, Como posso te ajudar? Converse comigo na forma imperativa, ou digite {bot.command_prefix}help para saber quais comandos posso executar"
      
      try:
        if ordem == "some":
          resultado = [int(termo) for termo in enunciado if termo.isnumeric()]
          resposta = f"O resultado dessa soma é {sum(resultado)}"
          await message.channel.send(resposta)

        elif ordem == "liste":
          await message.channel.send(enunciado)

        elif ordem == "imprima":
          await message.channel.send(" ".join(enunciado))

      except IndexError:
        await message.channel.send(hello)
