Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str=input("¿Cual es tu nombre ")
¿Cual es tu nombre 
>>> str=input("¿Cual es tu apellido paterno ")
¿Cual es tu apellido paterno 
>>> str=input("¿Cual es tu apellido materno ")
¿Cual es tu apellido materno 
>>> str=input("Dime tu edad ")
Dime tu edad 
>>> str=float(input("ingrese su peso en kilogramos: "))
ingrese su peso en kilogramos: 
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    str=float(input("ingrese su peso en kilogramos: "))
ValueError: could not convert string to float: ''
>>> str=input("ingresa tu peso en kilogramos ")
ingresa tu peso en kilogramos 
>>> str=input("ingresa tu estatura en centimetros ")
ingresa tu estatura en centimetros 
>>>  IMC = str("peso/estatura,2 ")
 
SyntaxError: unexpected indent
>>> str=IMC:input("peso/estatura,2 ")
SyntaxError: invalid syntax
>>> str=input("peso/estatura,2 ")
peso/estatura,2 
>>> print ("Hola "+"nombre "+"apellido "+"apellido "+"edad "+"IMC "
       