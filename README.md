# O poder da cobra: construindo uma rede social com Python e Django. 

Python é uma famosa linguagem de programação de alto nível, multiparadigma e de propósito geral. Com ela diversas empresas construíram e constroem, a um custo de desenvolvimento e manutenção baixo, a infra estrutura para os seus serviços. Dentre elas podemos destacar Google, Dropbox e Globo.com. O  Django, por usa vez, é um framework full stack para o desenvolvimento de aplicações web escrito em Python. Por se completo e fácil de usar, esse framework ganha cada vez mais importância no cenário atual de desenvolvimento ágil. O objetivo desse minicurso é apresentar a linguagem de programação Python em um nível básico, e com ela construir uma pequena rede social usando Django. Ou seja, o minicurso será dividido em uma primeira parte sobre a linguagem Python e a segunda o desenvolvimento web usando Django. 

## Sobre o autor :)

Analista de TI na Universidade Federal de Santa Maria (UFSM). Possui mestrado em ciência da computação pela mesma instituição, onde também fez graduação sanduíche em ciência da computação pelas universidades UFSM e Fachhochschule Gelsenkirchen (Alemanha). Atualmente, estuda desenho industrial e trabalha  desenvolvendo sistemas de gerenciamento do serviços de TI com Django na UFSM.

## Bibliografia de apoio

Boa parte do conteúdo desse minicurso foi baseado no livro [Python para desenvolvedores](http://ark4n.wordpress.com/python/) de Luiz Eduardo Borges. Esse é um bom livro de Python em portugues. A abordagem de Luiz Eduardo Borges em seu livro é prática e sem rodeios. O que permite um apredisado sem enrolação. 

Além disso, Osvaldo Santana Neto, que é um grande profissional muito conhecido na comunidade Python brasileira, disponibilisou um [curso de programação em Python e Django](https://osantana.me/curso-de-python-e-django/). Esse curso, em muitos momentos, serviu de inspiração e de material de apoio para a preparação do conteúdo deste minicurso.

A outra parte que iremos tratar, sobre Django, foi baseada na documentação oficial desse excepcional framework. O conte dos tutorial oficial pode ser encontrado no link: [https://docs.djangoproject.com/en/1.6/intro/tutorial01/](https://docs.djangoproject.com/en/1.6/intro/tutorial01/) 


# Conteúdo


## Python 

### Introdução

Python é uma linguagem de altíssimo nível (Very High Level Language) :

- **Multiparadigmas** (Procedural, Orientada a objeto e funcional)
- **Tipagem dinâmica e forte**
- **Abordagem híbrida (Interpretada + Compilada)**. A linguagem Python, assim como outras linguagens, apresenta um processo de compilação do código para um bytecode. Contudo,  diferente de outras linguagens, o processo de compilação é transparente para o desenvolvedor. Ou seja, não é necessário invocar o copilador. 

Histórico:

- Surgiu em **1991**
- Criado por **Guido van Rossen**
- Inspirado pelo **grupo de humor britânico Monty Python** 
- **Licença livre** compatível com a GPL
- Foco original em **físicos e engenheiros**

Versões:

- **2.7** foi lançado no meio de 2010. Essa é considerada a última versão da série 2.x.
- **3.0** foi lançada em 2008. A versão  mais recente é a **3.4** de 2014. Ela quebra retrocompatibilidade com a série 2.


> Guido van Rossum decidiu limpar Python 2.x de forma apropriada, com menos consideração para compatibilidade com versões anteriores do que é o caso de novos lançamentos na série 2.x. A melhoria mais drástica é o melhor suporte a Unicode (com todas as mensagens de texto sendo Unicode por padrão) bem como uma sensata separação de bytes/Unicode. [Python2orPython3](https://wiki.python.org/moin/Python2orPython3)

--- 

> Django 1.5 é a primeira versão do Django a suportar Python 3. O mesmo código roda em Python 2 (≥ 2.6.5) e Python 3 (≥ 3.2), graças a seis camadas de compatibilidade. [Django Porting to Python 3](https://docs.djangoproject.com/en/1.6/topics/python3/)
> - A versão atual do Django é a 1.6 e necessita apenas Python 2.6.5 (ou superior), sem a necessidade de bibliotecas adicionais.  


---
**Por hora** vamos nos focar em trabalhar com **Python 2.7**. Um ponto positivo é que em poucas horas de estudo é possível estar adaptado a série 3.x da linguagem.

---


### Quem usa python:

- Google
- Yahoo
- Nasa
- Instagram
- YouTube
- Dropbox
- Pintrest
- Prezi
- Spotify
- Disqus
- Pixar
- The Walt Disney Company 
- Call of Duty 4 (Moder Warfare)
- globo.com 
- Universidade Federal De Santa Maria - ufsm.br
- muitos outros

Nota: Parte do conteúdo desta seção (Quem usa python) foi retirado do curto [Python para Zumbis do Fernando Masanori](http://pycursos.com/python-para-zumbis/). 

---
> **Python me ajuda a focar nos meus conceitos em vez de ficar brigando com a linguagem** (Bruce Eckel, Autor do best seller “Thinking in Java” )

---

> **Pyton é rápido o suficiente para o nosso site e nos permite produzir características de fácil manutenção em tempos recordes, com um mínimo de desenvolvedores** (Cuong Do, Software Architect, Youtube)

---

> **[...] A nossa filosofica aqui é "Python sempre que pudermos, C++ se necessário".** (Alex Martelli, Líder técnico, Sistemas de produção, Google.)  

---
> **Python é uma das cinco mais importantes linguagens que todo o programador deve conhecer.** (Bjarne Stroustrup, criador da linguagem C++.)

___

### Cultura

O termo Pythonic é usado para indicar que algo é compatível com as premissas de projeto do Python.

**The Zen of Python**:

```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```


### Variáveis e Tipos

Nota: As explicações de variáveis e tipos dessata seção são baseadas na video aula [Python - Variáveis, Tipos de Dados e o comando Type](https://www.youtube.com/watch?v=SYioCdLPmfw).

Uma variável, dentro de um programa, é uma posição na memória que armazena um valor. A variável possui um nome identificador para permitir que o programado escrever códio para acessa e manipula os dados da variável durante a excecução do programa. As variáveis possuem um tipo. Esse tipo determina o tipo de informação que a variável irá armazenar.  

- Numéricos
    - Inteiro 
    - Ponto Flutuamte
- Lógicos
    - Booleano
- Literais
    - Caracteres e strings de caracteres
- Lista
- Tupla
- Dicionário


Os tipo de dados em Python podem ser:

1. **Mutáveis**: permitem que os conteúdos das variáveis sejam alterados.
1. **Imutáveis**: não permitem que os conteúdos das variáveis sejam alterados.


Uma variável em Python sempre deve ser inicializada. Ou seja, sempre que ela foi 
definida é necessário atribuir um valor para ela. Assim, a região da memória reservada para a 
memória irá ser inicializada. 

Crindo uma variável no interpretador Python: 

```
>>> x = 6
>>> x
6
>>> y = True
>>> y
True
>>> w = 5.0 
>>> w
5.0
>>> z = "Curso de python"
>>> z
'Curso de python'
```

É possível saber o tipo de uma variável usando a função *type()*.

```
>>> type(x)
<type 'int'>
>>> type(w)
<type 'float'>
>>> type(z)
<type 'str'>
```

O conteúdo referente a listas, tuplas e dicionários foi forte mente inspirado na documentação do site [py.franciscosouza.net](http://py.franciscosouza.net). Mesmo o site sendo antigo, todo o conteúdo foi testado e validado no python 2.7. :)

**Listas**: São conjuntos ordenados de valores, onde cada valor é identificado por um índide. Listas são similares a strings, que são conjuntos ordenados de caracteres, com a diferença que os elementos de uma lista podem possuir qualquer tipo.

Diferentemente das strings e das tuplas, as listas são mutaveis. Ou seja, é possível modificar seus elementos.

```
>>> lista = [1,2, 'Ana', 5.6, True]
>>> lista
[1, 2, 'Ana', 5.6, True]
>>> numeros = range(1,5)
>>> numeros
[1, 2, 3, 4]
>>> numeros[0]
1
>>> numeros[0] = 5
>>> numeros
[5, 2, 3, 4]
>>> numeros[-1]
4
>>> numeros[-2]
3
>>> len(numeros)
4
>>> numeros.append(10) #Listas são mutáveis
>>> numeros
[5, 2, 3, 4, 10]
>>> 5 in numeros #Verifica se o número 5 pertence a lista numeros
True
>>> cavaleiros = ['Athos', 'Porthos', 'Aramis']
>>> "D'Artagnan" not in cavaleiros
True
>>> cavaleiros = cavaleiros + ["D'Artagnan",] #Listas são mutáveis
>>> cavaleiros
['Athos', 'Porthos', 'Aramis', "D'Artagnan"]
```

Tupla é um tipo de dado que é similar a lista. No caso, a tupla apresenta a característica de ser  *imutável*.

```
>>> tupla = 'a', 'b', 'c', 'd', 'e'
>>> tupla
('a', 'b', 'c', 'd', 'e')
>>> tupla = ('a', 'b', 'c', 'd', 'e')
>>> tupla
('a', 'b', 'c', 'd', 'e')
>>> t1 = ('a',) #tupla com valor único
>>> tupla = ('A',) + tupla[1:] #A tupla é imutável, contudo é possível substituir uma tupla por outra
>>> tupla
('A', 'b', 'c', 'd', 'e')
```

As strings, listas e tuplas utilizam inteiros como indices. Já os dicionários utilizam qualquer tipo imutável de dados
como indice. Um dicionário vazio é declarado com o uso de {}.

```
>>> ing2esp = {}
>>> ing2esp['one'] = 'uno'
>>> ing2esp['two'] = 'dos'
>>> print ing2esp
{'two': 'dos', 'one': 'uno'}
```

Os elementos de um dicionário são separados por virculas e o indice é separado do valor através de dois pontos.  No caso os indices 
são chamados de chaves e os elementos de valor. Isso nos dá o conceito de chave-valor.

```
>>> ing2esp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
>>> print ing2esp
{'one': 'uno', 'three': 'tres', 'two': 'dos'}
>>> print ing2esp['two']
'dos'
>>> ing2esp.keys() #Retorna as chaves
['three', 'two', 'one']
>>> ing2esp.values() #Retorna os valores
['uno', 'tres', 'dos']
>>> ing2esp.items() #Retorna o conjunto chave-valor na forma de uma lista de tuplas
[('three', 'tres'), ('two', 'dos'), ('one', 'uno')]
>>> ing2esp.has_key('one')
True
>>> del ing2esp['one'] #Remove um elemento do dicinário
>>> print ing2esp
{'three': 'tres', 'two': 'dos'}
>>> ing2esp['four']='cuatro'
>>> ing2esp
{'four': 'cuatro', 'three': 'tres', 'two': 'dos'}
```


### Tipagem forte

> A tipagem do Python é forte, ou seja, o interpretador verifica se as operações são válidas e não faz coerções automáticas entre tipos incompatíveis. Para realizar a operação entre tipos não compatíveis, é necessário converter explicitamente o tipo da variável ou variáveis antes da operação.  ([Python para Desenvolvedores](http://ark4n.files.wordpress.com/2010/01/python_para_desenvolvedores_2ed.pdf))



### Tipagem dinâmica


> Python utiliza tipagem dinâmica, o que significa que o tipo de uma variável é inferido pelo interpretador em tempo de execução (isto é conhecido como Duck Typing). No momento em que uma variável é criada através de atribuição, o interpretador define um tipo para a variável, com as operações que podem ser aplicadas. ([Python para Desenvolvedores](http://ark4n.files.wordpress.com/2010/01/python_para_desenvolvedores_2ed.pdf))

Em muitos casos é comum de se atribuir a tendencia a erros de codificação no caso das liguagens que utilizam tipagem dinâmica. Afirma-se que a não declaração prévia do tipo gerar inconsistência nas operaçõe. Contudo, isso não diz respeito a tipagem dinâmica ou estática. Isso se refere se a linguagem é forte ou fracamente tipada. Na seção seguinte ([Tipagem Forte](#Tipagem forte)) abordamos essa questão em mais detalhes.

Contudo, uma questão que comumente gera erros de programação é a questão instanciação de variáveis de forma automática. A linguagem PHP, e em muitos casos, apresenta propensão para esse tipo de erro de programação, que são difíceis de serem identificados. De forma mais explícita, por exemplom, no caso de uma variável $nome_aluno ser intanciado com o nome "João"  e o programador for referenciar ela posteriormente como $nome_aulno acapaba passado desapercebido, pois a segunda referência é considerada uma nova variáve mesmo sendo evidente o erro de digitação. 


```
<?php

/**
* Variáveis em PHP são instanciadas de forma automática. 
* Isso acaba gerando uma maior propensão a erros de programação envolvendo 
* variáveis não inicializadas ou digitadas de maneira erronea. 
* Esses tipos de erros acabam ficando invisível ao programador, o que 
* torna mais difícil a depuração de sistemas. 
*/

$nome_aluno = "João";

echo $nome_aulno;

?>
```

``` 
# Python não instancia variávies de forma automática. 

>>> nome_aluno = u"João"
>>> print nome_aulno
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'nome_aulno' is not defined

```


### Tipagem forte

> A tipagem do Python é forte, ou seja, o interpretador verifica se as operações são válidas e não faz coerções automáticas entre tipos incompatíveis. Para realizar a operação entre tipos não compatíveis, é necessário converter explicitamente o tipo da variável ou variáveis antes da operação.  ([Python para Desenvolvedores](http://ark4n.files.wordpress.com/2010/01/python_para_desenvolvedores_2ed.pdf))

```
/* Exemplo de código de tipagem fraca em JavaScript */

> "5" + 2
"52"
> 2 + "5"
"25"
> "5" - 2
3
> 2 + ("5" - 1)
6
> "2" + ("5" - 1)
"24"
```

```
#Exemplo de tipagem fote com Python

>>> "5" + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects
>>> 2 + "5" 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> "5" - 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 2  + ( "5" - 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> "2" + ("5" - 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'int'
```

No caso dos exemplos acima, é possível perceber que o código JavaScript gera resultados diferentes para combinações de opeações envolvendo os mesmos tipos de dados. No primeiro caso existe a concatenação de uma string com um inteiro. O segundo comando basicamente é o primeiro em ordem invertida. Quando aplica-se um operador de subtração, o interpretador do JavaScript acaba convertendo o tipo do dado string para inteiro de forma automática. Por fim, **as duas útimas operações**, apresentadas no exemplo de JavaScript, mostram que **equações aparente mente iguais geram saidas completamente diferentes**, o que **resulta** em uma **inconsistência da linguagem**. Isso acaba gerando uma **série de erros de difícil identificação** no hora de programar uma aplicação. 

Já no caso do mesmo código feito em Python, em todos os casos o interpretador gerou uma saida de erro não permitindo que a operação fosse realizada. Para fazer a operação de dados com tipos diferentes é necessário fazer a conversão expĺícita de tipo, como no exemplo abaixo.

```
#Exemplo de tipagem fote com Python com conversão explícita de tipo

>>> "5" + str(2)
'52'
>>> 2 + int("5")
7
```

### Sintaxe 

Nota: Esta seção é adaptada do trabalho: ([Python para desenvolvedores](http://ark4n.wordpress.com/python/))

O caractere # marca o inicio de comentário. Qualquer texto depois do # será ignorado até o fim da linha, com exceção dos comentários funcionais. 

Comentários funcionais são usados para:
- alterar a codificação do arquivo fonte do programa acrescentando um comentário com o texto “#-*- coding: <encoding> -*#-” 
- definir o interpretador que será utilizado para rodar o programa em sistemas UNIX “#!” (#!/usr/bin/env python”)


Exemplo de comentários funcionais:
```
#!/usr/bin/env python
# -*- coding: latin1 -*-

# Uma linha de código que mostra o resultado de 7 vezes 3
print 7 * 3
```

Saída:

```
21

```

#### Bloco
Nota: Esta seção é adaptada do trabalho: ([Python para desenvolvedores](http://ark4n.wordpress.com/python/))

Em Python, os **blocos de código** são **delimitados pela indentação**, que deve ser constante no bloco de código, porém é considerada uma boa prática
manter a consistência no projeto todo e evitar a mistura tabulações e espaços. A [PEP8](http://legacy.python.org/dev/peps/pep-0008/), recomendação oficial de estilo de codificação, recomenda o uso de 4 espaços. 

> É importante configurar o editor de textos para tabular com espaços ao invés do caracter de tabulação. 

```
Instruçoes
Enquanto condição:
....Instruções
....Se condição:
........Instruções
....Senão:
........Instruções
Instruções
```
 
#### Condicional

```
if <condição>:
    <bloco de código>
elif <condição>:
    <bloco de código>
elif <condição>:
    <bloco de código>
else:
    <bloco de código>
```

1. <condição>: sentença que possa ser avaliada como verdadeira ou falsa
2. <bloco de código>: sequência de linhas de comando.
3. As clausulas elif e else são opcionais e podem existir vários elifs para o mesmo if, porém apenas um else ao final.
4. Parênteses só são necessários para evitar ambiguidades
Exemplo:
```
temp = int(raw_input('Entre com a temperatura: '))

if temp < 0:
    print 'Congelando...'
elif 0 <= temp <= 20:
    print 'Frio'
elif 21 <= temp <= 25:
    print 'Normal'
elif 26 <= temp <= 35:
    print 'Quente'
else:
    print 'Muito quente!'
```

Saída:

```
Entre com a temperatura: 23
Normal
```

Se o bloco de código for composto de apenas uma linha, ele pode ser escrito após os dois pontos:

```
if temp < 0: print 'Congelando...'
```

O python suporta a seguinte estrutura:

```
<variável> = <valor 1> if <condição> else <valor 2>
```
#### Laços
Nota: Esta seção é adaptada do trabalho: ([Python para desenvolvedores](http://ark4n.wordpress.com/python/))

Laços são estruturas de repetição.

##### For
A instrução aceita não só sequencias estáticas, mas também sequêncas geradas por iteradores. 

Clausula _break_ interrompe o laço e a _continue__ passa para a próxima interação. O códio dentro do else é executado ao final do laço, exceto se o laço tenha sido interrompido pelo _break_.

Sintaxe:

```
for <referência> in <sequência>:
	<bloco de código>
	continue
	break
else:
	<bloco de código>
``` 

Exemplo:

```
# Soma de 0 a 99
s = 0
for x in range(1,100):
    s = s + x

print s
```

Saída:
```
4950
```

##### While

Executa um bloco de código atendendo a uma condição.

Sintaxe:

```
while <condição>:
	<bloco de código>
	continue
	break
else:
	<bloco de código>
```
	
Exemplo:

```
# Soma de 0 a 99

s = 0 
x = 1 

while x < 100:
    s = s + x 
    x = x + 1
    
print s
```



#### Funções
Nota: Esta seção é adaptada do trabalho: ([Python para desenvolvedores](http://ark4n.wordpress.com/python/))

Funções são blocos de código identificadas por um nome, recebendo parâmetros pré-determinados

1. Podem reternar ou não objetos
2. Aceitam Doc Strings
3. Aceitam parâmetros opicionais (com **default**)
4. Aceitam que os **parâmetros sejam passados com nomes**. Neste caso, a ordem em que os parâmetros form passados não importa.
5. Podem ter suas propriedades alteradas (em geral, decoradores).

> Doc Strings são strings que estão associadas a uma estrutura do Python. Nas funções, as Doc Strings são colocadas dentro do corpo da função, geralmente no começo. O objetivo das Doc Strings é servir de documentação para aquela estrutura.

Sintaxe:

```
def func(parametro1, parametro2-padrao):
    """
    Doc String
    """
    <bloco de código>
    return valor
```

Exemplo:

```
# Fatorial implementado de forma recursiva
def fatorial(num):
    if num <= 1:
        return 1
    else:
        return (num * fatorial(num - 1))
        
# Testando fatorial()
print fatorial(5)
```

Saída:

```
120
```

Exemplo (Fibonacci sem recursão):

```
def fib(n):
    """
    Fibonacci:
    fib(n) = fib(n - 1) + fib(n - 2) se n > 1
    fib(n) = 1 se n <= 1 
    """
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1

# Mostrar Fibonacci de 1 a 5
for i in [1, 2, 3, 4, 5]:
    print i, '=>', fib(i)
```

Saída:

```
1 => 1
2 => 2
3 => 3
4 => 5
5 => 8
```

Exemplo (Conversão de RGB):

```
# -*- coding: utf-8 -*-

def rgb_html(r=0, g=0, b=0): 
    """
    Converte R, G, B em #RRGGBB
    """
    return '#%02x%02x%02x' % (r, g, b) 
def html_rgb(color='#000000'):
    """
    Converte #RRGGBB em R, G, B
    """
    if color.startswith('#'): 
        color = color[1:]
        r = int(color[:2], 16) 
        g = int(color[2:4], 16) 
        b = int(color[4:], 16)
    return r, g, b # Uma sequência

print rgb_html(200, 200, 255)
print rgb_html(b=200, g=200, r=255) # O que houve? 
print html_rgb('#c8c8ff')
```

Saída:

```
#c8c8ff
#ffc8c8
(200, 200, 255)
```

Exemplo de como receber todos parâmetros:

```
# -*- coding: utf-8 -*-
# *args - argumentos sem nome (lista)
# **kargs - argumentos com nome (dicionário)

def func(*args, **kargs): 
    print args
    print kargs
    
func('peso', 10, unidade='k')
```

Saída:

```
('peso', 10)
{'unidade': 'k'}
```

#### Documentação

Nota: Esta seção é adaptada do trabalho: ([Python para desenvolvedores](http://ark4n.wordpress.com/python/))

PyDOC é a ferramenta de documentação15 do Python. Ela pode ser utilizada tanto para acessar a documentação dos módulos que acompanham o Python, quanto a documentação dos módulos de terceiros

No Linux, a documentação das bibliotecas pode ser vista através do browser usando o comando:

```
￼￼pydoc -p 8000
```

O PyDOC utiliza as Doc Strings dos módulos para gerar a documentação.

### Exercícios 1 
Nota: Exercícios retirados do livro [Python para desenvolvedores](http://ark4n.wordpress.com/python/)

1. Implementar duas funções:
	1. Uma que converta temperatura em graus Celsius para Fahrenheit.
	1. Outra que converta temperatura em graus Fahrenheit para Celsius.
		> c = (5*(f-32)/9)
		
		> f = (9/5*c+32)
1. Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.
1. Implementar uma função que receba uma lista de inteiros e retorne a soma e a média dos valores. (Questão adaptada)
1. Crie uma função que:
	1. Receba uma lista de tuplas (dados), um inteiro (chave, zero por padrão igual) e um booleano (reverso, falso por padrão).
1.  Responda o que é tipagem forte e como isso influência na detecção de erros. (Exercício não tirado do livro)

> **Números primos** são os números naturais que têm apenas dois divisores diferentes: o 1 e ele mesmo.
> 
>  - 1 não é um número primo, porque ele tem apenas um divisor que é ele mesmo.
>  - 2 é o único número primo que é par.

#### Módulos

Nota: Esta seção é adaptada do trabalho: ([Python para desenvolvedores](http://ark4n.wordpress.com/python/))

Para o Python, módulos são arquivos fonte que podem importados para um programa. Podem conter qualquer estrutura do Python e são executados quando importados. Possuem namespace próprio e aceitam Doc Strings. São **objetos Singleton** (é carregada somente uma instância em memória, que fica disponível de forma global para o programa).

Os módulos são carregados através da instrução import. Desta forma, ao usar alguma estrutura do módulo, é necessário identificar o módulo. Isto é chamado de importação absoluta.

Módulos:

```
import os
print os.name
```

Importação de forma relativa:

```
from os import name
print name
```

O caracter * poder ser usado para importar dudo que está definido no módulo:
> NOTA: Nunca façam isso. :)
> 
> Por evitar problemas, como a ofuscação de variáveis, a importação absoluta é considerada uma prática de programação melhor do que a importação relativa.


```
form os import *
print name
```

Exemplo de módulo:

```
# -*- coding: utf-8 -*-
# mod_ex_media.py

def media(lista):
    return float(sum(lista))/len(lista)
```

Exemplo de uso do módulo:

```
# -*- coding: utf-8 -*-
# mod_ex_media_2.py

from mod_ex_media import media

lista = [23, 54, 31, 77, 12, 34]

print media(lista)
```

Saída:
```
38.5
```

O módulo principal de um programa tem a variável \_\_name\_\_ igual à “\_\_main\_\_”, então é possível testar se o módulo é o principal usando:

```
if __name__ == "__main__":
   #Se este for o módulo o principal este código será executado.

```
 
#### Pacotes

Nota: Esta seção é adaptada do trabalho: ([Python para desenvolvedores](http://ark4n.wordpress.com/python/))

**Pacotes (packages) são pastas** que são **identificadas** pelo interpretador pela presença de um arquivo com o nome **"\_\_\_init\_\_.py"**. Os pacotes funcionam como coleções para organizar módulos de forma hierárquica.

É possível importar todos os módulos do pacote usando a declaração from nome_do_pacote import *.

O arquivo **"\_\_init\_\_.py" pode estar vazioou conter código de inicialização do pacote**  ou definir uma variável chamada \_\_all\_\_, uma lista de módulos do pacote serão importados quando for usado “*”.


#### Orientação a Ojetos
##### Classes
Nota: Esta seção é adaptada do trabalho: ([Python para desenvolvedores](http://ark4n.wordpress.com/python/))

A classe é a estrutura básica do paradigma de orientação a objetos, que representa o tipo do objeto, um modelo a partir do qual os objetos serão criados. Objetos são abstrações computacionais que representam entidades, com suas qualidades (atributos) e ações (métodos) que estas podem realizar. 

sintaxe:

```
# -*- coding: utf-8 -*-
# Classe.py

class Classe(supcl1, supcl2): 
	"""
	Isto é uma classe 
	"""
	clsvar = []
	
	def __init__(self, args): 
		"""
		Inicializador da classe 
		"""
		<bloco de código>

	def __done__(self): 
		"""
		Destrutor da classe 
		"""
		<bloco de código>
		
	def metodo(self, params): 
		"""
		Método de objeto 
		"""
		<bloco de código>

	@classmethod
	def cls_metodo(cls, params): 
		"""
		Método de classe 
		"""
		<bloco de código>

	@staticmethod
	def est_metodo(params):
		"""
		Método estático 
		"""
		<bloco de código>


obj = Classe() 
obj.metodo()
Classe.cls_metodo() 
Classe.est_metodo()

```

Métodos de objeto podem usar atributos e outros métodos do objeto. A variável self, que representa o objeto e também precisa ser passado de forma explícita. O nome self é uma convenção, assim como cls, podendo ser trocado por outro nome qualquer, porém é considerada como boa prática manter o nome.

Métodos estáticos são aqueles que não tem ligação com atributos do objeto ou da classe. Funcionam como as funções comuns.


##### Métodos Especiais

Métodos especiais são identificados por nomes no padrão \_\_metodo\_\_() (dois sublinhados no início e no final do nome) e definem como os objetos derivados da classe se comportarão em situações particulares, como em sobrecarga de operadores.


##### Herança Simples

Herança é um mecanismo que a orientação a objeto provê, com objetivo de facilitar o reaproveitamento de código. A ideia é que as classes sejam construídas formando uma hierarquia.

A forma comum de herança é chamada de herança simples, na qual a nova classe é derivada de apenas uma classe já existente, porém é possível criar várias classes derivadas, criando uma hierarquia de classes.

Exemplo:

```
class Pendrive(object):
    def __init__(self, tamanho, interface='2.0'):
        self.tamanho = tamanho 
        self.interface = interface

class MP3Player(Pendrive):
    def __init__(self, tamanho, interface='2.0', turner=False):
        self.turner = turner
        Pendrive.__init__(self, tamanho, interface)
       
mp3 = MP3Player(1024)
print '%s\n%s\n%s' % (mp3.tamanho, mp3.interface, mp3.turner)
```

Saída:
```
1024 
2.0 
False
```


##### Sobrecarga de operadores

No Python, o comportamento dos operadores é definido por métodos especiais, porém tais métodos só podem ser alterados nas classes abertas. Por convenção, os métodos especiais têm nomes que começam e terminam com “__”.


| Operador     | Método          | Operação     |
| ------------ | --------------- | ------------ |
| +            | \_\_add\_\_     | Adição       |
| -            | \_\_sub\_\_     | Subtração    |
| *            | \_\_multi\_\_   | Multiplicação|
| /            | \_\_div\_\_     | Divisão      |
| ==           | \_\_eq\_\_      | Igual a      |
| <=           | \_\_le\_\_      | Meno ou igual|
| >=           | \_\_ge\_\_      | Maior ou igual |
| <            | \_\_lt\_\_      | Menor que    |
| >            | \_\_gt\_\_      | Maior que    |
| !=           | \_\_ne\_\_      | Diferente    |

Existem mais operadores ver lista em ([Python para desenvolvedores](http://ark4n.wordpress.com/python/)).

```
# A classe String deriva de str
class String(str):
    def __sub__(self, s):
        return self.replace(s, '')

s1 = String('The Lamb Lies Down On Broadway')
s2 = 'Down '

print '"%s" - "%s" = "%s"' % (s1, s2, s1 - s2)
```

Saída:
```
"The Lamb Lies Down On Broadway" - "Down " = "The Lamb Lies On Broadway"
```

#### Exercícios 2

Nota para resolver o exercício:
> 1. Crie um pacote para o projeto "universidade"
> 2. Crie um módulo chamado "Pessoas.py" (Crie as classes dentro deste arquivo)
> 3. Crie um arquivo separado chamado "principal.py" (Importe as classes e faça os testes neste arquivo) 


1. Crie uma classe Pessoa com os atributos nome e idade
	1. Sobre escreva o operador == para saber se duas pessoas são iguais. Serão considerados a mesma pessoa se tiverem o mesmo nome e idade.
	2 Crie uma lista com 5 pessoas compare ser se alguma pessoa aparece mais de uma vez. 	
2. Crie duas classes derivadas de pessoa: Aluno e Professo. 
	1. O aluno deve possuir os atributos matricula e ter uma lista de disciplinas matriculadas. 
	2. O progressor deve possuir uma lista de livros de bibliografia básica. 
	3. Crie 4 alunos e 2 professores.



## Django

A seção sobre django foi baseada na [documentação oficial](https://docs.djangoproject.com/en/1.6/intro/tutorial01/).

Vamos assumir que você já tenha o django instalado em sua máquina. Esse tutorial vai considerar o django 1.6. Apesar disso, acredito que tudo que está aqui irá funcionar na versão 1.7  sem nenhum impedimento. 

Vamos considerar duas partes: 

- A parte **pública do site**;
- A parte **administrativa**.

### Criando um projeto

Vamos iniciar a criação do projeto em **Django** usando um aplicativo escrito em python que nos gera a estrutura básica do projeto. Ele nos gera uma coleção de configurações para uma instancia do Django, incluíndo configuração do banco de dados, algumas opções específicas do Django e configurações de aplicativos.

```
django-admin.py startproject meusite
``` 

> Você deve evitar usar nomes que conflitem com outros aplicativos ou bibliotecas, como no caso de usar o nome _django_ ou _test_.

O projeto criato possui a seguinte estrutura:

```
meusite/
    manage.py
    meusite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
``` 

Algumas considerações:

- A pasta _meusite_ mais externa apenas armazena o seu projeto. 
- _manage.py_ é um script de linha de comando que ajuda você interagir com o seu projeto em diversas formas.
- A parta _meusite_  mais interna é um pacote Python do seu projeto. 
- meusite/__init__.py apenas define esse diretórico como um pacote Python válido.
- meusite/settings.py é o arquivo de configuração do projeto.
- meusite/urls.py contém as declações das urls desse projeto Django. Podemos considerar como o "índice" do seu projeto.
- meusite/wsgi.py é um ponto de entrada para deploy da aplicação para servidores conpatives com WSGI. 


### Servidor de desenvolvimento

Dentro do diretório base do seu projeto execute o comando: 

```
python manage.py runserver
```

Você irá perceber a seguinte saída:

```
Validating models...

0 errors found
September 10, 2014 - 02:45:52
Django version 1.6.5, using settings 'meusite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

Você acabou de iniciar o servidor de desenvolvimento web do Django. Ele é um servidor web puramente escrito em Python. Ele foi adicionando ao Django para permitir que o desenvolvedor possa se preocupar com a construção de seu projeto de forma rápida sem ter que lidar com as configurações de um servidor de produção - tal como o Apache - até ter que colocar o projeto em produção.

>  Não use esse serivodr embarcado para executar nada em produção. Ele foi adicionado apenas por conveniência para o desenvolvimento. 

Agora que o servidor está rodando visite http://127.0.0.1:8000/ em seu navegador. Você receberá uma tela de boas vindas do Django. 

Trocando a porta e o ip do servidor de desenvolvimento:

```
python manage.py runserver 8080
```

```
python manage.py runserver 0.0.0.0:8000
```

### Configuração do banco de dados

Agora é hora de irmos trabalhar com o nosso arquivo de configuração **meusite/settings.py**. 

Por padrão a configuração utiliza  o SQLite. Para inicar a desenvolver e conhecer Django essa é maneira mais fácil. SQLite é incluído no Python, dessa forma você não precisa instalar nada para dar suporte ao seu banco de dados. 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

- **ENGINE**:  representa o drive do Django responsável por conectar no banco de dados e dar suporte ao ORM. Pode ser:  'django.db.backends.sqlite3', 'django.db.backends.postgresql_psycopg2', 'django.db.backends.mysql' ou 'django.db.backends.oracle'. Existem outros bancos disponíveis. 
- **NAME**: O nome do seu banco de dados. No caso do SQLite ele será um arquivo em seu computador. Sendo o SQLite, é necessário que essa variável possua o endereço completo até o arquivo. 

Se você não estiver usando o SQLite como seu banco de dados será necessário adicionar **USER**, **PASSWORD** e **HOST**.

No caso precisa trocar a lingua da nossa aplicação. Também não vamos usar timezone. Dessa forma, vamos setar essas variáveis da seguinte maneira: 

```
LANGUAGE_CODE = 'pt-br'

USE_TZ = False 
```

As outras definções vamos deixar da forma que estão.

Note que existe uma tupla chamada INSTALLED_APPS. Ela contém o nome das aplicações em Django que estarão ativas para essa instância do Django. Aplicações podem ser utilizadas em múltiplos projetos e você pode distribuir elas para outros usuários utilizarem em seus projetos. 

Por padrão o chando ativa os seguintes apps:

- django.contrib.admin
- django.contrib.auth
- django.contrib.contenttypes 
- django.contrib.sessions
- django.contrib.messages
- django.contrib.staticfiles

Esses aplicativos são incluídos por padrão como conveniência para os casos mais comuns. 


Para criar as tabelas do banco de dados, vamos utilizar o seguinte comando:

```
python manage.py syncdb
```

Esse comando confere as aplicações que estão definidas na variável **INSTALLED_APPS** do settings e cria as tabelas necessárias. 


### Criando modelos

Cada aplaicação que você escreve em Django consiste em um pacote que segue uma certa convensão.  O Django vem com uma ferramenta que constrói o diretório e a estrutura base da aplicação.

Para criar a sua aplicação nós vamos executar o seguinte comando:

```
python manage.py startapp enquetes
```

Ele irá criar um diretório **enquetes** que contém:

```
enquetes/
    __init__.py
    admin.py
    models.py
    tests.py
    views.py
```

Essa estrutura de diretórios irá abrigar a sua aplicação. 

A primeira coisa em escrever um aplicativo web que acesso o banco de dados em Django é definir o modelo. Basicamente o modelo contém o layout do seu banco de dados com metadados adicionais. 

> Filosofia:
> Um modelo é a única e definitiva fonte de especificaço dos seus dados. Ele contém os campos e o comportamento dos dados que você está armazenando. O Django segue o princípio [DRY (Don’t repeat yourself)](https://docs.djangoproject.com/en/1.6/misc/design-philosophies/#dry). O objetivo é definir o modelo de dados em um local e derivar as coisas automaticamente dai.

Em nosso exemplo nós iremos criar dois modelos: **Enquete** e **Escolha**. 

```
# coding: utf-8
from django.db import models 

class Enquete(models.Model):
    questao = models.CharField(max_length=200)
    data_de_pubicacao = models.DateTimeField(u'Date de publicação')

class Escolha(models.Model):
    enquete = models.ForeignKey(Enquete)
    texto_da_escolha = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

```

O código é direto. Cada modelo é representado por uma classe que herda 
**django.db.models.Model**. Cada modelos tem um número de variáveis de classe, cada um representa um campo do bando de dados no modelo.

Cada campo é representado por uma instância de **Field**, por exemplo: **CharField** para campos de caracteres e **DateTimeField** para data e hora. Isso informa ao Django qual é o tipo de dados de cada campo.

A opção **max_length** definie o tamanho máximo que o campo CharField consegue armazenar. 

A opcão **default** define o valor inicial. Nesse caso nós definimos como 0 o valor inicial para o número de votos. 

Finalmente, a relação entre as classes é feita através do campo **ForeignKey**. Isso informa ao Django que cada **Escolha** está relacionada a apenas uma **Enquete**. 

Algúns dos campos mais utilizados:

- models.BooleanField()
- models.CharField()
- models.DateTimeField()
- models.EmailField()
- models.FileField()
- models.FloatField()
- models.ImageField()
- models.IntegerField()
- models.IPAddressField()
- models.PositiveIntegerField()
- models.TextField()
- models.URLField()
- models.ForeignKey()
- models.ManyToManyField()


Algumas das opções mais utilizadas para configurar um campo:

- null
- max_length (CharField e outros)
- blank
- choices
- default
- help_text
- unique
- verbose_name
- auto_now_add (DateTimeField e outros)
- upload_to (ImageField, FileField e outros)


### Ativando os modelos

Um pouco de código do modelos provê o Django com muita informação. Com isso o Django é acapaz de:

- Criar o schema do banco de dados (CREATE TABLE ...)
- Criar uma API de acesso aso dados em Python através dos objetos **Enquete** e **Escolha**.

Mas primeiro é necessário informar o nosso projeto que a aplicação *enquetes** está instalada. Para fazer isso basta adicionar o _settings.py_ e adicionar no final da tupla INSTALLED_APPS o item "enquetes".

```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'enquetes',
)

```

Agora que temos a aplicação **enquetes** instalados, vamos executar o comando:

```
python manage.py sql enquetes
```

Você deve ver algo similar com o seguinte código sql:

```
BEGIN;
CREATE TABLE "enquetes_enquete" (
    "id" integer NOT NULL PRIMARY KEY,
    "questao" varchar(200) NOT NULL,
    "data_de_publicacao" datetime NOT NULL
)
;
CREATE TABLE "enquetes_escolha" (
    "id" integer NOT NULL PRIMARY KEY,
    "enquete_id" integer NOT NULL REFERENCES "enquetes_enquete" ("id"),
    "texto_da_escolha" varchar(200) NOT NULL,
    "votos" integer NOT NULL
)
;

COMMIT;

```

Perceba o seguinte:

- O nome das tabelas irá ser gerado automaticamente da combinação do nome da aplicação (enquetes) com o nome do modelo - enquete e escolhas.
- A chave primária é automaticamente gerada.
- Por convensão o Django adiciona "_id" ao nome do campo da chave estrangeira.
- O comando **sql** não executa esse código **SQL** em sua base de dados. Apenas imprime na tela o SQL que o Django cria. 


Agora vamos sincronizar os nossos modelos com o bando de dados. Execute o comando:

```
python manage.py syncdb
```

O comando **syncdb** executará a sincronização do banco de dados apenas para as aplicações que ainda não foram sincronizadas. 


### Brincando com a API

Agora vamos nos dirigir ao interpretador python do django. Use o comando:

```
python manage.py shell
```

Nós estamos utilizando o shell do django apenas por que ele já adiciona nas variáveis de ambiente as aplicações instaladas no nosso arquivo **meusite/settings.py**.

```
>>> from enquetes.models import Enquete, Escolha
>>> 
>>> Enquete.objects.all()
[]

# Vamos criar uma enquete.
>>> from django.utils import timezone
>>> e = Enquete(questao=u"Qual é a novidade?", data_de_publicacao=timezone.now())

# Salve a enquete no banco.
>>> e.save()

# Após a execução do método save nós podemos verificar que a nossa enquete possui
# um id.
>>> e.id
1

# verificando qual é a questão
>>> e.questao
u'Qual \xe9 a novidade?'

# verificando a data de publicação
>>> e.data_de_publicacao
datetime.datetime(2014, 9, 10, 4, 44, 39, 751061, tzinfo=<UTC>)

# Mudando o atributo e salvando no banco de dados usando o método save()
>>> e.questao = "E ae?"
>>> e.save()

# objects.all() mostra todas as enquetes que estão armazenadas no banco de dados

>>> Enquete.objects.all()
[<Enquete: Enquete object>]

```

### Conhecendo o painel administrativo do Django 

### Escreva a sua primeira View (Rotas)

### Escrevendo mais Views

### Templates








## Exercício Final:

Crie um projeto chamado **socialsati**.
- Defina as configurações:
```
LANGUAGE_CODE = 'pt-br'

USE_TZ = False 
```
- Verifique se o banco de dados é o SQLite
- Mantendo as apliações que já estão definidas, sincronize o projeto com o banco de dados.
- Crie duas aplicações
    - perfies
    - postagens

- Na aplicação **perfies** defina os seguintes campos:
    - nome_cidade: charfield com tamanho máximo de 32 caracteres
    - usuario: sendo esse uma ForeignKey para ->  from django.contrib.auth.models import User. Definir o atributo **related_name** para related_name='perfil'  
    - foto: ImageFiel para fazer upload para "perfis/%Y/%m/%d/%h"
    - seguindo: sendo um campo ManyToMany para from django.contrib.auth.models import User. Definir o atributo **related_name** para related_name='seguido'

- Na aplicação **postagens** defina os seguintes campos:
    - postado_por: Sendo esse uma ForeignKey para ->  from django.contrib.auth.models import User.
    - conteudo: Sendo um CharField que aceita no máximo de 140 caracteres. 
    - data: adicione a esse campo o auto_now_add=True




```
# talvez precise do summetrical = False

 follow = models.ManyToManyField('self', symmetrical=False, related_name='user_follow')
    followed_by = models.ManyToManyField('self', symmetrical=False, blank=True , related_name='user_followed_by')
```

 






