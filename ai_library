# Matemática
def soma_lista(termos):
  """Soma todos os itens numéricos da lista de termos"""
  resultado = [int(termo) for termo in termos if termo.isnumeric()]
  return f"O resultado dessa soma é {sum(resultado)}"


# Gerenciamento
def enquete(termos):
  import re

  """Cria uma enquete binária a partir da lista de termos"""
  frase = " ".join(termos)
  # pega o índice de '?'
  if '?' in frase:
    interrogacao = re.search("\?", frase)
    pergunta = frase[:interrogacao.start()+1]
  else:
    pergunta = "Não existe enquete"
  
  return f"Enquete: {pergunta}"
