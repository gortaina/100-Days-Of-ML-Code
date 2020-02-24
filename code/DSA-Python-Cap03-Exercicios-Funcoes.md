
# <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 3</font>

## Download: http://github.com/dsacademybr

## Exercícios - Métodos e Funções


```python
# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e 
# depois faça uma chamada à função para listar os números  
```


```python
def lista20():
    for i in range(1,20):
        print (i)
        
lista20() 
```


```python
# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string
```


```python
def toCAP(word):
    print(word.upper())
    
toCAP("little ground")
```


```python
# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista
```


```python
def addLista(lista):
    print ("tipo de obj ",type(lista))
    lista.append(["new1", "new2"])
    print ("lista nova ", lista)
    
list1 = [1,2,3,4]    
addLista(list1)
addLista([5,6,7,"8oito"])

```

    tipo de obj  <class 'list'>
    lista nova  [1, 2, 3, 4, ['new1', 'new2']]
    tipo de obj  <class 'list'>
    lista nova  [5, 6, 7, '8oito', ['new1', 'new2']]
    


```python
# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos
```


```python
def recebeLista(lista1, *listaN):
    print ("lista1 %r listaN %r", lista1, listaN)
    
recebeLista(["N"])
recebeLista(["N"],["D","E"],["a","b","c","d"])
```

    lista1 %r listaN %r ['N'] ()
    lista1 %r listaN %r ['N'] (['D', 'E'], ['a', 'b', 'c', 'd'])
    


```python
# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles
```


```python
soma = lambda x,y: x+y
print (soma(6,8))
```

    14
    


```python
# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;


soma( 10, 20 );
print ("Fora da função o total é: ", total)
```

    Dentro da função o total é:  30
    Fora da função o total é:  0
    


```python
# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
Celsius = [39.2, 36.5, 37.3, 37.8]
#Fahrenheit = map(coloque_aqui_sua_função_lambda)
#print (list(Fahrenheit))
```


```python
#help(map)
Fahrenheit2 = map(lambda c:c*1.8+32, Celsius)
print (list(Fahrenheit2))
```

    [102.56, 97.7, 99.14, 100.03999999999999]
    


```python
# Exercício 8
# Crie um dicionário e liste todos os métodos e atributos do dicionário
```


```python
dic1 = {"key1":100,"key2":200,"key3":300,"key4":400,}

for k,v in dic1.items():
    print("keys",k)
    print("values", v)
    
```

    keys key1
    values 100
    keys key2
    values 200
    keys key3
    values 300
    keys key4
    values 400
    


```python
# Exercício 9
# Abaixo você encontra a importação do Pandas, um dos principais pacotes Python para análise de dados.
# Analise atentamente todos os métodos disponíveis. Um deles você vai usar no próximo exercício.
import pandas as pd
dir(pd)
```




    ['Categorical',
     'CategoricalIndex',
     'DataFrame',
     'DateOffset',
     'DatetimeIndex',
     'ExcelFile',
     'ExcelWriter',
     'Expr',
     'Float64Index',
     'Grouper',
     'HDFStore',
     'Index',
     'IndexSlice',
     'Int64Index',
     'Interval',
     'IntervalIndex',
     'MultiIndex',
     'NaT',
     'Panel',
     'Period',
     'PeriodIndex',
     'RangeIndex',
     'Series',
     'SparseArray',
     'SparseDataFrame',
     'SparseSeries',
     'Term',
     'TimeGrouper',
     'Timedelta',
     'TimedeltaIndex',
     'Timestamp',
     'UInt64Index',
     'WidePanel',
     '_DeprecatedModule',
     '__builtins__',
     '__cached__',
     '__doc__',
     '__docformat__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__path__',
     '__spec__',
     '__version__',
     '_hashtable',
     '_lib',
     '_libs',
     '_np_version_under1p10',
     '_np_version_under1p11',
     '_np_version_under1p12',
     '_np_version_under1p13',
     '_np_version_under1p14',
     '_np_version_under1p15',
     '_tslib',
     '_version',
     'api',
     'bdate_range',
     'compat',
     'concat',
     'core',
     'crosstab',
     'cut',
     'date_range',
     'datetime',
     'datetools',
     'describe_option',
     'errors',
     'eval',
     'factorize',
     'get_dummies',
     'get_option',
     'get_store',
     'groupby',
     'infer_freq',
     'interval_range',
     'io',
     'isna',
     'isnull',
     'json',
     'lib',
     'lreshape',
     'match',
     'melt',
     'merge',
     'merge_asof',
     'merge_ordered',
     'notna',
     'notnull',
     'np',
     'offsets',
     'option_context',
     'options',
     'pandas',
     'parser',
     'period_range',
     'pivot',
     'pivot_table',
     'plot_params',
     'plotting',
     'pnow',
     'qcut',
     'read_clipboard',
     'read_csv',
     'read_excel',
     'read_feather',
     'read_fwf',
     'read_gbq',
     'read_hdf',
     'read_html',
     'read_json',
     'read_msgpack',
     'read_parquet',
     'read_pickle',
     'read_sas',
     'read_sql',
     'read_sql_query',
     'read_sql_table',
     'read_stata',
     'read_table',
     'reset_option',
     'scatter_matrix',
     'set_eng_float_format',
     'set_option',
     'show_versions',
     'test',
     'testing',
     'timedelta_range',
     'to_datetime',
     'to_msgpack',
     'to_numeric',
     'to_pickle',
     'to_timedelta',
     'tools',
     'tseries',
     'tslib',
     'unique',
     'util',
     'value_counts',
     'wide_to_long']




```python
# ************* Desafio ************* (pesquise na documentação Python)

# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo 
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"
import pandas as pd
file_name = "binary.csv"
```


```python
#help(pd.DataFrame)
#help(pd.read_csv)
df = pd.read_csv(file_name)
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>admit</th>
      <th>gre</th>
      <th>gpa</th>
      <th>rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.600000</td>
      <td>616.000000</td>
      <td>3.480000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.547723</td>
      <td>185.148589</td>
      <td>0.421307</td>
      <td>1.224745</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>380.000000</td>
      <td>2.930000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
      <td>520.000000</td>
      <td>3.190000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.000000</td>
      <td>640.000000</td>
      <td>3.610000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1.000000</td>
      <td>660.000000</td>
      <td>3.670000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.000000</td>
      <td>880.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
    </tr>
  </tbody>
</table>
</div>



# Fim

### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
