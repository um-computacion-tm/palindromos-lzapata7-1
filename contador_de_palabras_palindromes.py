def cantidad_de_palabras_palindromes(palabras):
    contador = 0
    for palabra in palabras:
        palabra = palabra.replace(" ","").replace(",","").replace("-","").lower()
        if palabra == palabra[::-1]:
            contador += 1
    return contador