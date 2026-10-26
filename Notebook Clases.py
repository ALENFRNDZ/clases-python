# variables --> nombre = valor

nombre = "Alén Fernández"

# Tipos de variables
    nombre = "Alen Fernández" # tipo string
    edad = 32 #tipo int
    salario = 150.50 # tipo float

# para conocer el tipo de variables:
print (edad, type(edad))

# operadores matemáticos
    suma_numero = 10 + 3  # + realiza sumas
    resta_numero = 10 - 3  # + realiza resta
    producto_numero = 10 * 3  # + realiza multiplicaciones
    division_numero = 10 / 3  # + realiza divisiones
    division_entera_numero = 10 // 3  # + realiza la division entera (sin resto)
    modulo_numero = 10 % 3  # + realiza modulo (muestra solo el resto)

# operadores lógicos y de comparación

    Los **booleanos** (bool) representan datos `True` (Verdadero) o `False` (Falso), y suelen aparecer al realizar operaciones lógicas

    numero_1 = 10
    numero_2 = 1000
    numero_1 < numero_2  # True (menor que)
    numero_1 <= numero_2  # True (menor o igual que)
    numero_1 > numero_2  # False (mayor que)
    numero_1 >= numero_2  # False (mayor o igual que)
    numero_1 != numero_2  # True (no igual que) con la palabra clave `is not`
    numero_1 is not numero_2
    numero_1 == numero_2  # False (igual que) con la palabra clave `is`
    numero_1 is numero_2


# Los tipos de variables tiene métodos asociados, que son funciones que se aplican a un tipo de variable concreto. 
# Por ejemplo, los strings tienen métodos como: 
# `upper()` para convertir a mayúsculas, 
# `lower()` para convertir a minúsculas, 
# `strip()` para eliminar espacios al principio y al final, 
# etc.

    nombre = "Alén Fernández"
    print(nombre.upper())  # ALÉN FERNÁNDEZ
    print(nombre.lower())  # alén fernández
    print(nombre.strip())  # Alén Fernández

# f strings son una forma de formatear strings en Python, permitiendo incluir variables dentro de cadenas de texto de manera sencilla y legible. 
# Se utilizan colocando una `f` antes de las comillas y usando llaves `{}` para insertar las variables.

    saludo = f"Hola! Mi nombre es {nombre.title()}"
    print(saludo)


    # Cuándo f-strings son útiles:
        #- Cuando necesitas incluir variables dentro de cadenas de texto.

    # Cuando + es útil:
        #- Cuando quieres concatenar cadenas de texto y variables.

    # Con +
    saludo = "Hola! Soy " + nombre.title() + " y tengo " + str(edad) + " años."

    # Con f-string
    saludo = f"Hola! Soy {nombre.title()} y tengo {edad} años."

    #Ambos producen el mismo resultado. Como regla práctica: f-strings para mensajes; + para uniones sencillas de textos.


# Tipos complejos de variables

    #Listas
    lista = [1, 2, 3, 4, 5, "Alén", 3.14, True]

    #Diccionarios
    diccionario = {"clave": "valor"}

    diccionario = {
        "nombre": "Alén",
        "edad": 32,
        "salario": 150.50,
        "casado": True
    }
    print(diccionario["clave"])  # valor

    print(diccionario["nombre"])  # Alén
    print(diccionario["edad"])  # 32
    print(diccionario["salario"])  # 150.50
    print (diccionario["casado"])  # True

    print(diccionario) #Alén, 32, 150.50, True

    #Tuplas
    tupla = (1, 2, 3, 4, 5, "Alén", 3.14, True)
    Las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación.
    A diferencia de las listas, que son mutables y permiten cambios en sus elementos.
    Un ejemplo de esto es que no se pueden agregar, eliminar o modificar elementos en una tupla después de su creación, mientras que en una lista sí se pueden realizar estas operaciones.

    Una lista se modifica de esta forma:
    lista = [1, 2, 3]
    y una tupla se define de esta forma:
    tupla = (1, 2, 3)




# Bloques

# Control de flujos
    #Bucles
    lista = [1,2,3,4,5,6,7,8]

    #Bucle while

    n = 0
    while n <= 5:
        n+=1
        print(n)

    #Bucle for

    lista = [1,2,3,4,5,6,7,8]
    for numero in lista:
        print(numero)


if nombre == "Alén Fernández":
    print("Hola")

# funciones --> nombre()

