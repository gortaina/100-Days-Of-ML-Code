
# <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 3</font>

## Download: http://github.com/dsacademybr

## Exercícios - Loops e Condiconais


```python
# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
```


```python
dia = input("Qual dia da semana? ").lower()

if dia == "domingo" or dia == "sábado":
    print("Hoje é dia de descanso")
else:
    print("Você precisa trabalhar!")     
```

    Qual dia da semana?Domingo
    Hoje é dia de descanso
    


```python
# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
```


```python
listFruit = ["Laranja", "Maçã", "Banana", "Pera", "Morango", "Figo"]
if listFruit.count("Morango") > 0:
    print ("Morango está na lista")
else:
    print ("Morango NÃO está na lista")
```

    Morango está na lista
    


```python
# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista
```


```python
tup1 = (3,6,9,12)
list2 = []
for i in tup1:
    list2.append(i*2)
    
print (list2)

```

    [6, 12, 18, 24]
    


```python
# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
```


```python
for i in range (100,151,2):
    print(i)
```

    100
    102
    104
    106
    108
    110
    112
    114
    116
    118
    120
    122
    124
    126
    128
    130
    132
    134
    136
    138
    140
    142
    144
    146
    148
    150
    


```python
# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela
```


```python
temperatura = 40
while temperatura > 35:
    print (temperatura)
    temperatura -= 1
```

    40
    39
    38
    37
    36
    


```python
# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa
```


```python
contador = 0
while contador < 100:
    print (contador)
    if contador == 23:
        break
    contador += 1

        
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    


```python
# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista
```


```python
list7 = []
#list7 = list()
var1 = 4
while var1 <= 20:
    if (var1%2 == 0):
        list7.append(var1)
    var1 += 1
print ("Lista par",list7)
```

    Lista par [4, 6, 8, 10, 12, 14, 16, 18, 20]
    


```python
# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = range(5, 45, 2)
```


```python
nums = range(5, 45, 2)
list8 = []
for i in range(5, 45, 2):
    list8.append(i)

print(list8)
#ou usando uma função
print(list(nums))
```

    [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43]
    [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43]
    


```python
# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30
print('Vista roupas leves.')
else
    print('Busque seus casacos.')
```


```python
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')
```

    Qual a temperatura? 29
    Busque seus casacos.
    


```python
# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a 
# vantagem de existir.” (Machado de Assis)

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir." 
```


```python
frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir." 
contador = frase.count('r')
print("Total de r é %r " %contador)

#ou usando um loop for
contador = 0
for caracter in frase:
    if caracter == 'r':
        contador += 1
print("O Total de r é %r " %contador)        
```

    Total de r é 6 
    O Total de r é 6 
    

# Fim

### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
