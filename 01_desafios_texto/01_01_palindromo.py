palabra_elegida = input("Escribe una palabra: ")

def es_palindromo(palabra_elegida):
    palabra_minuscula = palabra_elegida.lower()
    texto_sin_espacios = palabra_minuscula.replace(" ", "")
    return texto_sin_espacios == texto_sin_espacios[::-1]

print(es_palindromo(palabra_elegida))