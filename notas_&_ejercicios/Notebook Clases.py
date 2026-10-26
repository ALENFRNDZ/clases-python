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


    #Los tipos complejos de variables(listas[], tuplas() y diccionarios{}) también tienen métodos asociados.
       
        #metodos de tuplas
            #.count(valor) ---> Cuenta el número de repeticiones de ese valor/objeto
            #.index(valor) ---> Indica el índice de ese valor, pero solo la primera vez que ha sido encontrado

        #metodos de listas
            #.count(valor) ---> Cuenta el número de repeticiones de ese valor/objeto
            #.index(valor) ---> Indica el índice de ese valor, pero solo la primera vez que ha sido encontrado        
            #.append(valor) ---> Añade al final de la lista ese valor/objeto (su referencia)
            #.insert(int, valor) ---> Añade en la posicion int ese valor/objeto (su referencia)
            #.extend(iterable) ---> Concatena un iterable (cualquier iterable) con esa lista
            #.clear() ---> Vacia la lista
            #.copy() ---> Crea una copia de esa lista (id() sera distinto para copias, siendo pues dos objetos distintos)
            #.pop(int) ---> Elimina el valor en el indice int, por defecto el último elemento
            #.remove(valor) ---> Elimina la primera vez que encuentra ese valor
            #.reverse() ---> Invierte la lista
            #.sort(bool, funcion) ---> Ordena la lista. Este método es poderoso pero complejo, permite indicar si se ordena de menor a mayor, o al reves (reversed), y permite especificar un método de ordenación bastante complejo y poderoso
       
        #metodos de diccionarios
            #.get(clave, valor) ---> Extrae valor de esa clave, y si no la encuentra, muestra valor
            #.setdefault(clave, valor) ---> Extrae valor de esa clave, y si no la encuentra, crea una clave-valor
            #.clear() ---> Vacia el diccionario
            #.copy() ---> Hace una copia del diccionario
            #.pop(clave, valor) ---> Elimina esa clave, y si no la encuentra, muestra valor
            #.update(diccionario) ---> Actualiza un diccionario con nuevas clave-valor
            #.values() ---> Extrae los valores de ese diccionario
            #.keys() ---> Extrae las claves de ese diccionario
            #.items() ---> Extrae tuplas (clave, valor) de ese diccionario
            #.fromkeys(iterable, valor) ---> Crea un diccionario formando claves con el iterable, y con un mismo valor (definido en el método)



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


#Tipos de errores en python
    #Existen varios tipos de errores en Python, algunos de los más comunes son:
    
        - SyntaxError: #Error de sintaxis, ocurre cuando el código no sigue las reglas del lenguaje.
        - NameError: #Error de nombre, ocurre cuando se intenta usar una variable o función que no ha sido definida.
        - TypeError: #Error de tipo, ocurre cuando se realiza una operación con un tipo de dato incorrecto.
        
        - ValueError: #Error de valor, ocurre cuando se pasa un valor incorrecto a una función.
        - IndexError: #Error de índice, ocurre cuando se intenta acceder a un índice que no existe en una lista o tupla.
        - KeyError: #Error de clave, ocurre cuando se intenta acceder a una clave que no existe en un diccionario.
        - AttributeError: #Error de atributo, ocurre cuando se intenta acceder a un atributo que no existe en un objeto.
        


# funciones --> nombre()

#Las funciones son bloques de código reutilizables que realizan una tarea específica. 
# Se definen utilizando la palabra clave `def`, seguida del nombre de la función y paréntesis. 
# Pueden aceptar parámetros y devolver valores.

def mi_funcion():
    print("Hola, soy una función")

#Las funciones deben llamarse o invocarse para que tengan efecto

mi_funcion()  # Llamada a la función

#Hay 4 tipos de funciones, de acuerdo a: 1,2 si tienen (o no) un return, o 3,4 si tienen (o no) argumentos.

La keyword return devuelve un valor desde la función

def suma_dos_numeros():
    numero_1 = int(input("Primer numero: "))
    numero_2 = int(input("Segundo numero: "))
    return numero_1 + numero_2  # Especificamos que devuelva la suma de los dos numeros

mi_suma = suma_dos_numeros()  # Se guarda en una variable el return de la funcion
print(mi_suma)

#Las funciones pueden tener argumentos, que son valores que se pasan a la función para que los utilice en su ejecución.

def suma_dos_numeros(numero_1, numero_2):  # Estos son sus dos argumentos
    return numero_1 + numero_2

mi_suma = suma_dos_numeros(13, 5)  # Y aqui se le pasan dos parametros, 13 y 5
print(mi_suma)
mi_otra_suma = suma_dos_numeros(mi_suma, 10)
print(mi_otra_suma)