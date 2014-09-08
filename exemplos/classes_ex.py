# -*- conding: utf-8 -*-

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
