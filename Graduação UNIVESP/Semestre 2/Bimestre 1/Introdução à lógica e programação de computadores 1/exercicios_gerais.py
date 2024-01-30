# Este arquivo foi criado para o registro e execução dos exercícios propostos na disciplina intitulada de Algoritmos e Programação de Computadores I, do 2 semestre de 2024, oferecido pela UNIVESP

# Semana 1

## Instrução: Pratique o conteúdo da semana fazendo os exercícios do livro Algoritmos: lógica para desenvolvimento de programação de computadores, que seguem abaixo:

### Exercício 1. Cap. 3 – Ex 4a

#### Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é F ← C * 9 / 5 + 32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

# Primeiro, vamos definir uma função que converta os valores de Celsius para Fahrenheit
def converter_fahrenheit(celsius):
    fahrenheit = (celsius* 9/5) + 32
    return fahrenheit

# Agora, vamos solicitar ao usuário que passe uma temperatura em Celsius
temperatura_celsius = float(input('Por favor, digite a temperatura em Celsius que você deseja converter para Fahrenheit: '))

temperatura_fahrenheit = converter_fahrenheit(temperatura_celsius)
print('A temperatura de ' + str({temperatura_celsius}) + ' graus Celsius equivale a ' + str({temperatura_fahrenheit}) + ' graus em Fahrenheit')


### Exercício 2.6

#### Primeiro, execute a atribuição palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']. Agora, escreva duas expressões Python que são avaliadas, respectivamente, como a primeira e a última palavras em palavras, na ordem do dicionário.

palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']

# Expressão para obter a primeira palavra em ordem do dicionário
primeira_palavra = sorted(palavras)[0]

# Expressão para obter a última palavra em ordem do dicionário
ultima_palavra = sorted(palavras)[-1]

print(f"A primeira palavra em ordem do dicionário é: {primeira_palavra}")
print(f"A última palavra em ordem do dicionário é: {ultima_palavra}")


### Exercício 2. Cap. 4 – Ex 3c

#### Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno representadas pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética (variável MD) desse aluno e apresentar a mensagem “Aluno Aprovado com média” se a
#### média obtida for maior ou igual a 5; caso contrário, apresentar a mensagem “Aluno Reprovado com média”. Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno.

# Primeiro, vamos criar uma função para calcular a média aritmética das notas do aluno
def calcular_media(n1, n2, n3, n4):
    notas = (n1, n2, n3, n4)
    soma_notas = sum(notas)
    MD = soma_notas/4
    return MD

def verificar_aprovacao(MD):
    if MD > 5:
        print('Aluno aprovado com média ' + str(MD))
    else:
        print('Aluno reprovado com média ' + str(MD))
        

# Agora vamos solicitar que a pessoa entre os valores de nota do aluno
n1 = float(input('Por favor, digite a nota que o aluno tirou no primeiro bimestre: '))
n2 = float(input('Por favor, digite a nota que o aluno tirou no segundo bimestre: '))
n3 = float(input('Por favor, digite a nota que o aluno tirou no terceiro bimestre: '))
n4 = float(input('Por favor, digite a nota que o aluno tirou no quarto bimestre: '))

# Agora vamos aplicar a função nas notas do aluno e verificar se ele foi aprovado ou reprovado
MD = calcular_media(n1, n2, n3, n4)
verificar_aprovacao(MD)





