#!/usr/bin/env python
from time import sleep
from random import choice
import os


print('''
    [01] ALEATORIO                         [02] MAYUSCULAS
    [03] MINUSCULAS                        [04] NUMEROS
    [05] SIMBOLOS                          [06] MAYUSCULAS Y MINUSCULAS
    [07] MAYUSCULAS MINISCULAS Y NUMEROS   [08] MINUSCULAS Y NUMEROS
    [09] MAYUSCULAS Y NUMEROS              [10] AlfName
           ''')

os.system('chmod 777 -R *')
try:
    inicial = str(input("Ingresa un numero --> "))
    print('\n\n[#]Ejmplo: 10 = abcdefghij\n\n')
    numero = int(input("Ingresa cantidad de letras--> "))



    def aleatoria ():
    	while True:
    		try:
    			claves = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ=.,(_)/[]"

    			space = ""

    			space = space.join([choice(claves) for i in range(numero)])


    			f = open ("password.txt", 'a')
    			f.write(space)
    			f.write("\n")
    			print(space)
    		except KeyboardInterrupt:
    			break


    #ALEATORIOS DIC
    def mayuscula ():
    	while True:
    		try:
    			claves = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    			space = ""

    			space = space.join([choice(claves) for i in range(numero)])


    			f = open ("password_mayuscula.txt", 'a')
    			f.write(space)
    			f.write("\n")
    			print(space)
    		except KeyboardInterrupt:
    			break


    #MAYUSCULAS
    def minusculas ():
    	while True:
    		try:

    			claves = "abcdefghijklmnnopqrstuvwxyz"

    			space = ""

    			space = space.join([choice(claves) for i in range(numero)])


    			f = open ("password_minusculas.txt", 'a')
    			f.write(space)
    			f.write("\n")
    			print(space)
    		except KeyboardInterrupt:
    			break

    #MINUSCULAS
    def numerico ():
    	while True:
    		try:

    			claves = "0123456789"

    			space = ""

    			space = space.join([choice(claves) for i in range(numero)])


    			f = open ("password_numerico.txt", 'a')
    			f.write(space)
    			f.write("\n")
    			print(space)
    		except KeyboardInterrupt:
    			break

    #NUMEROS
    def simbolos ():
    	while True:
    		try:

    			claves = "<, .>;/][-=!@#$%^&*()}_+{|"

    			space = ""

    			space = space.join([choice(claves) for i in range(numero)])


    			f = open ("password_simbolos.txt", 'a')
    			f.write(space)
    			f.write("\n")
    			print(space)
    		except KeyboardInterrupt:
    			break

    #SIMBOLOS
    def mayusculaandminusculas ():
    	while True:
    		try:
    			claves = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    			space = ""

    			space = space.join([choice(claves) for i in range(numero)])


    			f = open ("mayusculas;minusculas.txt", 'a')
    			f.write(space)
    			f.write("\n")
    			print(space)
    		except KeyboardInterrupt:
    			break


    #MAYUSCULAS Y MINUSCULAS
    def mayusculaandminusculasandnumeros ():
    	while True:
    		try:

    			claves = "1234567890abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    			space = ""

    			space = space.join([choice(claves) for i in range(numero)])


    			f = open ("mayusculas;minusculas;numeros.txt", 'a')
    			f.write(space)
    			f.write("\n")
    			print(space)
    		except KeyboardInterrupt:
    			break

    #MAYUSCULAS MINISCULAS Y NUMEROS
    def minusculasandnumeros ():
    	while True:
    		try:

    			claves = "abcdefghijklmnñopqrstuvwxyz1234567890"

    			space = ""

    			space = space.join([choice(claves) for i in range(numero)])


    			f = open ("minusculas;numeros.txt", 'a')
    			f.write(space)
    			f.write("\n")
    			print(space)
    		except KeyboardInterrupt:
    			break

    #MINUSCULAS Y NUMEROS
    def mayusculasandnumeros ():
    	while True:
    		try:

    			claves = "1234567890ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    			space = ""

    			space = space.join([choice(claves) for i in range(numero)])


    			f = open ("mayusculas;numeros.txt", 'a')
    			f.write(space)
    			f.write("\n")
    			print(space)
    		except KeyboardInterrupt:
    			break

    #MAYUSCULAS Y NUMEROS
    def xname ():

    	claves = str(input("\n\nEjmplo anonimo etc etc\nEsto devolvera datos aleatorio\nIngresa palabras a mezclar --->  "))
    	while True:
    		try:

    			space = ""

    			space = space.join([choice(claves) for i in range(numero)])


    			f = open ("personal.txt", 'a')
    			f.write(space)
    			f.write("\n")
    			print(space)
    		except KeyboardInterrupt:
    			break

    if inicial == '1':
    	aleatoria()
    elif inicial == '2':
    	mayuscula()
    elif inicial == '3':
    	minusculas()
    elif inicial == '4':
    	numerico()
    elif inicial == '5':
    	simbolos()
    elif inicial == '6':
    	mayusculaandminusculas()
    elif inicial == '7':
    	mayusculaandminusculasandnumeros()
    elif inicial == '8':
    	minusculasandnumeros()
    elif inicial == '9':
    	mayusculasandnumeros()
    elif inicial == '10':
    	xname()

except KeyboardInterrupt:
    print('\n\n[+]Saliendo del script')
    sleep(2)
    os.system('clear')
    False
