# O poder da cobra: construindo uma rede social com Python e Django. 

Python é uma famosa linguagem de programação de alto nível, multiparadigma e de propósito geral. Com ela diversas empresas construíram e constroem, a um custo de desenvolvimento e manutenção baixo, a infra estrutura para os seus serviços. Dentre elas podemos destacar Google, Dropbox e Globo.com. O  Django, por usa vez, é um framework full stack para o desenvolvimento de aplicações web escrito em Python. Por se completo e fácil de usar, esse framework ganha cada vez mais importância no cenário atual de desenvolvimento ágil. O objetivo desse minicurso é apresentar a linguagem de programação Python em um nível básico, e com ela construir uma pequena rede social usando Django. Ou seja, o mini curso será dividido em uma primeira parte sobre a linguagem Python e a segunda o desenvolvimento web usando Django. 

## Sobre o autor :)

Analista de TI na Universidade Federal de Santa Maria (UFSM). Possui mestrado em ciência da computação pela mesma instituição, onde também fez graduação sanduíche em ciência da computação pelas universidades UFSM e Fachhochschule Gelsenkirchen (Alemanha). Atualmente, estuda desenho industrial e trabalha  desenvolvendo sistemas de gerenciamento do serviços de TI com Django na UFSM.

## Bibliografica de apoio

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

- Surgiu em **1989**
- Criado por **Guido van Rossen**
- Inspirado pelo **grupo de humor britânico Monty Python** 
- **Licença livre** compatível com a GPL
- Foco original em **físicos e engenheiros**

Versões:

- **2.7** foi lançado no meio de 201. Essa é considerada a última versão da série 2.x.
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

* Listas: É um conjunto ordenado de valores, onde cada valor é identificado por um índide. Listas são similares a strings, que são conjuntos ordenados de caracteres, com a diferença que os elementos de uma lista podem possuir qualquer tipo.

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


### Tipagem dinâmica

> Python utiliza tipagem dinâmica, o que significa que o tipo de uma variável é inferido pelo interpretador em tempo de execução (isto é conhecido como Duck Typing). No momento em que uma variável é criada através de atribuição, o interpretador define um tipo para a variável, com as operações que podem ser aplicadas. ([Python para Desenvolvedores](http://ark4n.files.wordpress.com/2010/01/python_para_desenvolvedores_2ed.pdf))


### Tipagem forte

> A tipagem do Python é forte, ou seja, o interpretador verifica se as operações são válidas e não faz coerções automáticas entre tipos incompatíveis. Para realizar a operação entre tipos não compatíveis, é necessário converter explicitamente o tipo da variável ou variáveis antes da operação.  ([Python para Desenvolvedores](http://ark4n.files.wordpress.com/2010/01/python_para_desenvolvedores_2ed.pdf))


### Sintaxe 

#### Como é um programa em Python

O Python utiliza a própria identação para a definição de blocos. No caso a [PEP8](http://legacy.python.org/dev/peps/pep-0008/) recomenda nunca usar o caracter de tabulação para fazer a codifição de dos blocos lógiso. Ao invés da tabulação recomendase configurar o editor de texto para se dar 4 espaços.
  

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# o caracter '#' tem a função de comentário de linha
# fib.py - é um pequeno programa em python que retorna a sequencia de fibonacci  
"""
Fibonacci 
"""
def fib(valor):
    resultado = []
    a, b = 0, 1
    while b <= valor:
        resultado.append(b)
        a, b = b, a+b
    return resultado

valor = int(raw_input("Digite o valor: "))
print fib(valor)

```

#### Estruturas de controle

#### Orientação a Ojetos
##### Métodos Especiais
##### Herança Simples
##### Herança Múltipla
##### Sobrecarga de operadores
##### Meta Classes

#### Módulos
TODO: Explicar como são os módulos.
TODO: Apresentar os principais módulos da linugagem Python.


## Djanto

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












 






