# -*- coding: utf-8 -*-
# *args - argumentos sem nome (lista)
# **kargs - argumentos com nome (dicionário)

def func(*args, **kargs): 
    print args
    print kargs
    
func('peso', 10, unidade='k')

