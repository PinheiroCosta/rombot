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
        """ Reação do bot às mensagens do usuario"""

        # Aguarda a mensagem do usuario
        await bot.process_commands(message)

        # Identifica o autor
        autor = message.author
        # Identifica a mensagem
        msg = message.content
        # TODO: separar esse bloco de if na funcao cria_enquete()
        if message.author == bot.user:
            """ Adiciona enquete no chat, se o autor da mensagem for o bot. """
            if msg.split()[0] == "Enquete:":
                await message.add_reaction('\N{THUMBS UP SIGN}')
                await message.add_reaction('\N{THUMBS DOWN SIGN}')
            return

        # retorna mensagem caso seja mencionado
        if str(bot.user.id) in message:
            greeting = ["Oi", "Olá", "Falae", "Salve", "Ei"]
            ordem = message.split()[1]
            enunciado = message.split()[2:]
            hello = f"{random.choice(greeting)} {autor.name},",
            "Como posso te ajudar? Converse comigo na forma imperativa,",
            "ou digite {bot.command_prefix}help para saber quais",
            "comandos posso executar"

        try:
            await message.channel.send(speech_option(ordem, enunciado))

        except IndexError:
            await message.channel.send(hello)

        except KeyError:
            await message.channel.send(hello)
