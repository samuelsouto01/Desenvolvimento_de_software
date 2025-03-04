#        ||  Orientação a Objetos  ||
#  A Orientação a Objetos surgiu com a finalidade de representar melhor o mundo em que vivemos, melhorando a organização dos nossos projetos, facilitando a depuração e correções
# é um campo de estudo em que determina as funcionalidades e características de um determinado Objeto da vida real

# Suponhamos que queira criar uma variavel para guardar os dados de meus animais de estimação em um sistema de PetShop, por exemplo
# sem os conceitos de orientação a objetos teriamos que criar varias linhas de código apenas para guardar estas informações, repetidas vezes durante o desenvolvimento do sistema
# A partir dos Conceitos apresentados nesse tópico você será capaz de realizar possiveis alterações ou manutenção em apenas uma parte do código que será aplicadas a todas as 'instancias'
# desse objeto.

# Um Objeto é representado por Classes em linguagens de programação, Ex:
class Filhote():
  def __init__(self, nome, brinquedo_favorito):
    self.nome = nome
    self.brinquedo_favorito = brinquedo_favorito

  def brincar(self):
    print(f" O {self.nome} está brincando com {self.brinquedo_favorito}!")

# a partir do código acima é possivel criar varias 'instancias' com caracteriscas distintas entre eles, mas o que seria a 'instância', seria basicamente uma variavel cuja a atribuição
# é feita com um classe específica
#    Observe o uso de palavras específicas como '__init__' ou 'self', não se preocupe com esses termos por enquanto. É apenas uma convenção para a criação de Objetos padronizados por 
# diversos programadores. 
#       - A palavra '__init__' define qual a inicialização do objeto na hora que fazemos a instanciação desse.
#       - A palavra 'self' é apenas uma refêrencia a instancia.

chico = Filhote('Chico', 'urso de pelúcia')
chico.brincar()

#              || Modulos ||

# módulos são arquivos separados que facilitam a compreensão e alteração do código por outros programadores, uma convenção entre os desenvolvedores.
# existem por padrão alguns módulos já pré definidos, as bibliotecas padrões, por exemplo a biblioteca 'random' responsável por gerir números pseudo-aleatórios, Ex:

import random

#   A partir desse código é como se eu tenha pego todas as linhas de códigos presente na biblioteca padrão 'random' e inserido no meu arquivo, ai então eu consigo executar as funções
# definidas na biblioteca. Podemos analizar quais bibliotecas padrões o Python nos fornece procurando por Documentação Python em qualquer plataforma de busca (Google) ou diretamente 
# pelo site "https://docs.python.org/3/" para a versão 3 do Python

# agora podemos continuar a utilizar as funções da biblioteca 'random', suponhamos que eu queira embaralhar uma sequencia de números em uma lista, podemos ulilizar a função 'shuffle'
lista = [1,2,3,4,5]
print(lista)
random.shuffle(lista)
print(lista)

# podemos aprender como utilizar as bibliotecas visitando a documentação para Python, mas e se eu quiser escolher um número dentre essa lista, utilizando a função random.choice()
numero = random.choice(lista)
print(numero)



