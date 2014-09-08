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
>>> import thisThe Zen of Python, by Tim Peters

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
Namespaces are one honking great idea -- let's do more of those!```


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

1. **Mutáveis**: permitem que os conteúdos das variáveis sejam alterados.1. **Imutáveis**: não permitem que os conteúdos das variáveis sejam alterados.


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
print 7 * 3```

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
    <bloco de código>```

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
# -*- coding: utf-8 -*-def rgb_html(r=0, g=0, b=0): 
    """
    Converte R, G, B em #RRGGBB
    """    return '#%02x%02x%02x' % (r, g, b) 
def html_rgb(color='#000000'):    """    Converte #RRGGBB em R, G, B    """    if color.startswith('#'): 
        color = color[1:]        r = int(color[:2], 16) 
        g = int(color[2:4], 16) 
        b = int(color[4:], 16)    return r, g, b # Uma sequênciaprint rgb_html(200, 200, 255)
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
# -*- coding: utf-8 -*-# *args - argumentos sem nome (lista)# **kargs - argumentos com nome (dicionário)def func(*args, **kargs):     print args
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
1. Crie uma função que:	1. Receba uma lista de tuplas (dados), um inteiro (chave, zero por padrão igual) e um booleano (reverso, falso por padrão).
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
	"""	Isto é uma classe 	"""	clsvar = []
		def __init__(self, args): 		"""		Inicializador da classe 		"""		<bloco de código>	def __done__(self): 		"""		Destrutor da classe 		"""		<bloco de código>
			def metodo(self, params): 		"""		Método de objeto 		"""		<bloco de código>	@classmethod	def cls_metodo(cls, params): 		"""		Método de classe 		"""
		<bloco de código>	@staticmethod	def est_metodo(params):		"""		Método estático 		"""		<bloco de código>


obj = Classe() 
obj.metodo()Classe.cls_metodo() Classe.est_metodo()

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
class Pendrive(object):    def __init__(self, tamanho, interface='2.0'):        self.tamanho = tamanho 
        self.interface = interfaceclass MP3Player(Pendrive):    def __init__(self, tamanho, interface='2.0', turner=False):        self.turner = turner        Pendrive.__init__(self, tamanho, interface)
       mp3 = MP3Player(1024)print '%s\n%s\n%s' % (mp3.tamanho, mp3.interface, mp3.turner)
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
| <            | \_\_le\_\_      | Menor que    |
| >            | \_\_lt\_\_      | Maior que    |
| !=           | \_\_ne\_\_      | Diferente    |

Existem mais operadores ver lista em ([Python para desenvolvedores](http://ark4n.wordpress.com/python/)).

```
# A classe String deriva de strclass String(str):    def __sub__(self, s):        return self.replace(s, '')s1 = String('The Lamb Lies Down On Broadway')s2 = 'Down 'print '"%s" - "%s" = "%s"' % (s1, s2, s1 - s2)```

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

### Criando um projeto

### Servidor de desenvolvimento

### Configuração do banco de dados

### Criando modelos

### Ativando os modelos

### Brincando com a API

### Conhecendo o painel administrativo do Django (Apenas introdutório)

### Escreva a sua primeira View (Rotas)

### Escrevendo mais Views

### Templates











 






