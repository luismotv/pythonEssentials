# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 19:18:44 2021

@author: luism
"""
#Parte 1
#Usar la instrucción print para imprimir cadenas de texto
print('Empezando a trabajar con Python')
print('Realizado por: Luis Otero')

#Usar print para imprimir espacios en blanco con saltos de línea
print('')
print('')

print('Consultando los tipos de valores')
print('')

#Usar la intrucción type para determinar el tipo de un número entero
print('El tipo de dato de 875 es: ', type(875))
print('')

#Usar la instrucción type para determinar el tipo de una cadena de texto
print('El tipo de dato del texto: Now is better than never. es: ', type('Now is better than never.'))
print('')

#Usar la instrucción type para determinar el tipo de un número flotante
print('El tipo de dato de 1.32 es: ', type(1.32))
print('')

#usar la instrucción isinstance para determinar si 5+8i es un número entero o no
print('¿El valor 5 + 8i corresponde a un valor entero? ', isinstance('5+8i', int))
print('')

#Usar la instrucción isinstance para determinar si 8.2 es un número entero o no
print('¿El valor 8.2 corresponde a un valor entero? ', isinstance(8.2, int))
print('')

#Usar la instrucción isinstancepara determinar si Readability counts es una cadena de texto
print('¿El texto: Readability counts. corresponde a un string? ', isinstance('Readability counts', str))    
print('')
print('')
print('-----------------------------------------------------------------------')

#Parte 2
print('Programa que identifica el tipo de dato de un valor ingresado por el usuario, se realizarán cinco interacciones:')
print('')

#Crear una variable llamada dato1 que guarde el valor que el usuario ingresa a través de la instrucción input
dato1 = input('Primera interacción Ingrese un valor cualquiera: ')
print('Este tipo de dato es: ', type(dato1))
print('')

#Crear una variable llamada dato2 que guarde el valor que el usuario ingresa a través de la instrucción input
dato2 = input('Segunda interacción Ingrese un valor cualquiera: ')
print('Este tipo de dato es: ', type(dato2))
print('')

#Crear una variable llamada dato3 que guarde el valor que el usuario ingresa a través de la instrucción input
dato3 = input('Tercera interacción Ingrese un valor cualquiera: ')
print('Este tipo de dato es: ', type(dato3))
print('')

#Crear una variable llamada dato1 que guarde el valor que el usuario ingresa a través de la instrucción input
dato4 = input('Cuarta interacción Ingrese un valor cualquiera: ')
print('Este tipo de dato es: ', type(dato4))
print('')

#Crear una variable llamada dato5 que guarde el valor que el usuario ingresa a través de la instrucción input
dato5 = input('Quinta interacción Ingrese un valor cualquiera: ')
print('Este tipo de dato es: ', type(dato5))
print('')
print('¡YA NO SE HARÁN MÁS INTERACCIONES!')

