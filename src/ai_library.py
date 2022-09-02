import re


# Matemática
def soma_lista(conjunto):
    """Soma todos os itens numéricos do conjunto"""

    resultado = [int(termo) for termo in conjunto if termo.isnumeric()]
    return f"O resultado dessa soma é {sum(resultado)}"


# Gerenciamento
def enquete(conjunto):
    """Cria uma enquete binária a partir do conjunto"""

    frase = " ".join(conjunto)
    # pega o índice de '?'
    if '?' in frase:
        interrogacao = re.search("\?", frase)
        pergunta = frase[:interrogacao.start()+1]
    else:
        pergunta = "Não existe enquete"

    return f"Enquete: {pergunta}"
