# Alumno: Lucas Zapata
Ingenieria Informatica
## Codigo comentado para entender el funcionamiento.
### Palabras Palindromas
    def is_palindrome(value):
        # Imprime el valor recibido en la función
        print(value)
        # Imprime el valor invertido [::-1]
        print(value[::-1])
        # Compara el valor original con el valor invertido
        if value == value[::-1]:
            # Si son iguales, devuelve True
            return True
        else:
        # Si no son iguales, devuelve False
        return False
### Contador de Palabras Palindromas
    def cantidad_de_palabras_palindromes(palabras):
        # Inicializa un contador para llevar la cuenta de palabras palíndromas
        contador = 0
        # Itera sobre cada palabra en la lista de palabras
        for palabra in palabras:
            # Limpia la palabra eliminando espacios, comas y guiones, y la convierte a minúsculas
            palabra = palabra.replace(" ","").replace(",","").replace("-","").lower()
            # Comprueba si la palabra es un palíndromo comparándola con su inversa
            if palabra == palabra[::-1]:
              # Si la palabra es un palíndromo, incrementa el contador en 1
                contador += 1
        # Devuelve la cantidad total de palabras palíndromas encontradas
        return contador
## Para comprobar si funciona
    -Realizar un git clone (link con el SSH del repo) en la carpeta donde quieras almacenar el archivo.
    -Una vez con los direcctorios en su computadora los busca en la terminal usando cd (nombre de la carpeta donde se encuentra el archivo)
    -Ya en la carpeta donde se encuentra el archivo ejecutamos python3 test_palindromos.py (en el caso de que se quiera ejecutar el programa de Palabras Palindromas)
    -Luego si queremos ejecutar el Contador de palabras palindromas, se ejecuta de la misma manera pero con el nombre del archivo correspondiente (python3 test_contador_de_palabras_palindromes.py)
    -Luego de esto y finalmente se ejecutaran los test para comprobar si los codigos funcionan correctamete.

