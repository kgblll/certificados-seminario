#!/usr/bin/python
# -*- coding: utf-8 -*-
# Este generador de certificados de asistencia lee una lista con nombre, grado y deni
# para rellenarlos en una plantilla LaTeX con un marcador para cada campo.
# Opcionalemente compila los ficheros LaTeX generados y los une en uno solo.
# Si la plantilla LaTeX da error de compilación, pulsar intro varias veces.

import codecs

print "Pyasistencia: Generador de certificados de asistencia en formatos LaTeX y pdf.\n"

# Invocar al terminal
from commands import *
import commands
def run_command(cmd):
	getstatusoutput(cmd)

# Cargar lista de nombres
lista = codecs.open("listadip.csv", "r", encoding="utf8").readlines()

#contador
a = 100

for line in lista: # para cada persona...
	a += 1 #contador
	b = str(a) #pasa el contador a cadena
	salida = codecs.open("output" + b + ".tex", "w", encoding="utf8") # crea fichero LaTeX para cada persona
	person = line[0:-1].split(u",") # pasar la cadena en lista
	print person

	text = codecs.open("asistencia.tex", "r", encoding="utf8") # abrir documento LaTeX
	text = text.read() # leer documento LaTeX
	text_list = text.split(" ") # pasa a lista de palabras

	text_list[text_list.index(u"%pointnombre},")] = person[0] + u"}," # inserta nombre
	text_list[text_list.index(u"%pointgrado}")] = person[3] + u"}"  # inserta grado
	text_list[text_list.index(u"%pointdni},")] = person[1] + u"},"  # inserta dni

	text_final = u" ".join(text_list) # de lista a cadena

	print [text_final]

	salida.write(text_final) # guarda los cambio en el fichero creado
	salida.close() # cierra el fichero creado

	run_command(str("pdflatex " + "output" + b + ".tex")) # compila el fichero LaTeX a pdf (opcional)
	print person[0] #control

run_command(str("pdftk output*.pdf cat output todos_diplomas.pdf")) # crea pdf con todos los diplomas creados (opcional)

print "\n¡FINAL DE LA OPERACIÓN!" #control
