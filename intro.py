#                    || introdução a linguagem Python ||
#    - conceitos básicos da linguagem
#    - Operações aritmeticas ( '+' => soma , '-' => subtração, '/' => divisão, '*' => multiplicação)
#    - Operações de comparação ('==' igualdade , '!=' => diferença , '>' => maior que, '<' => menor que)
#                                  OBS: podemos utilizar a igualdade junto com o maior que ou menor que. EX '>=' maior que ou igual.
#    - Tipos de dados: inteiros, floats (numeros com virgula, neste caso o ponto), Caracter 'a' ,Strings (cadeia de caracteres "Samuel"), 
# Boolean (Verdadeiro ou falso ex "True"), Listas e dicionarios.
#  A linguagem Python não é altamente tipada, ou seja uma variavel (que varia ou não com o decorrer do programa) pode assumir diferentes 
# tipos de dados ao decorrer da execução
#
#            ||  Primeiros comandos com o python ||
#     - função 'print', é uma palavra reservada para 'imprimir' um dado na tela, Ex:

print(" Olá Mundo!")

# observe a sintaxe da linguagem presente na linha de código acima ao ser executado retorna a frase que está escrita entre aspas duplas ou simples
# agora vamos aprender um pouco mais sobre variaveis e atribuições

nome = "Samuel Souto"
print(nome)

# o que resultou no código acima?
# mas e se eu quiser que o usuario insira o seu nome como proceder?
#    - Função 'input', é responsavel pela entrada de dados pelo usuário. Ex:

nome = input("Digite o seu nome: ")
print(nome)

#    - Condicionais, assim como nós no dia a dia tomamos decisões o computador também executa operações lógicas e verifica se uma 
# determinada expressão é verdadeira ou não. ultilizamos então algumas funções booleanas existentes na linguagem como:
#  - fução 'if', que verifica se dada comparação é verdadeira

nome = "Samuel Souto"
if (nome == null):
  print(" Nome incorreto ou vazio")

# ao executar esse código obtemos um resultado? o que aconteceu? 
# exatamente nada, pois a condição não foi satisfeita.
# a palavra reservada 'null' é utilizada para descrever um cenário onde falta alguma informação. Geralmente associada a errros de 
# digitação ou até mesmo a existencia de arquivos ou diretorios, por exemplo, suponhamos que queira abrir um arquivo no meu computador
# pode ser que este arquivo não exista ou exista em outro local, assim teremos a resposta como null, abordaremos alternativas no decorrer
# do curso.

# - função 'elif', é uma alternativa caso a primeira condição não seja satisfeita

nome = "Samuel Souto"
if (nome == null):
  print(" Nome incorreto ou vazio")
elif (nome == "Samuel Souto"):
  print(" Este é o idealizador do nosso projeto")
else:
  print(nome)

# Observe outra função no código acima
#  - função 'else', dada uma comparação ela executa caso as comparações anterior da função if e elif não é satisfeita

#    - iteração: 'while' ou 'for', é uma função que executa um determinado código repetidas vezes até satisfazer determinada condição

cont = 5
while cont >= 0:
  print(cont)
  cont = cont - 1

#   observe a interação do comando while, é executada enquanto tal condição não é atingida se retirarmos a incrementação do cont, 
# nosso programa ira rodar indefinitivamente

for e in nome:
  print(e)

#   Observe que o comando while tem a necessidade de alterar a variavel observada, enquanto o comando 'for' se auto incrementa


#                 || Funções ||
#  atá aqui você desenvolveu habilidades básicas como imprimir um texto ou resultado, armazenar um dado, e inserir novos dados.
# mas e se quiser perguntar novamento o nome do usuario, terei que reescrever todo o código, as funções servem para evitar esse problema
# exemplo: as funções aprendidas até agora executam outros comandos já pré determinados.
#   Observe a sintaxe da criação de uma nova função

def qual_seu_nome():
  nome = input("Digite o seu nome: ")
  return nome

#   observe que a partir do codigo acima tem varias palavras reservadas e até mesmo o uso de outra função já conhecida.
# a partir de agora não temos a necessidade de reescrevermos estas linhas de código, podendo simplesmente fazer a refencia 
# a esse bloco de código, exemplo:

nome = qual_seu_nome()
print(nome)

# essa funçao simples pode ser melhorada, conferindo se o dado realmente é um nome, porém isso sera revisado com o decorrer do curso
# essa função não possuí nenhum tipo de dado parâmetro como as nossas funções já conhecidas. Ex 'print'

#      || Listas ||

# uma lista em Python é definida por colchetes '[]', utiliza-se para armazenar sequencias de dados de maneira mais prática, ex:
numero_de_nomes = 1
lista_de_nomes = []

while numero_de_nomes < 3:
  lista_de_nomes.append(input(f"Digite o {numero_de_nomes}º nome: "))

#   Observe a execução do código acima, o que está acontecendo?
# isso mesmo esquecemos de incrementar o nosso contador 'cont', seria somar 1 a nossa variavel de controle 'cont' ao decorrer dos passos

numero_de_nomes = 1
lista_de_nomes = []

while numero_de_nomes < 3:
  lista_de_nomes.append(input(f"Digite o {numero_de_nomes}º nome: "))
  cont += 1 

# agora podemos continuar os estudos
# nesse bloco há uma nova função aprendida a função .append() , mas o que isso siginifica?
# é uma função que está associada ao objeto 'list', falaremos sobre objetos no proximo capítulo, a principio entenda como uma das 
# funções básica das listas

#      ||  Dicionários ||
#  Um dicionário é quase uma lista, só que com chaves {}, onde cada chave possuí um identificador e seu respectivo dado, estes separados
# por dois pontos ':', EX:

meu_dicionario = {'nome': 'Samuel Souto', 'idade' : 27 }
print(meu_dicionario['idade'])

# observe que podemos adicionar mais chaves e determinar seu conteudo:
meu_dicionario['cor'] = 'Parda'
print(meu_dicionario['cor'])

# Também podemos remover uma determinada chave com a funçao '.pop'
meu_dicionario.pop('cor')
print(meu_dicionario)

