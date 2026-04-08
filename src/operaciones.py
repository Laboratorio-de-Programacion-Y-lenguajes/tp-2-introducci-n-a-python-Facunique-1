# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo.
    Ignora espacios, puntuación y mayúsculas.
    
    Lógica:
    1. Convierte a minúsculas
    2. Elimina espacios y caracteres no-alfabéticos
    3. Compara con su inversa
    
    Ejemplos:
    - es_palindromo("Anita lava la tina") → "anitalavalatina" == "anitalavalatina" ✓
    - es_palindromo("hola") → "hola" ≠ "aloh" ✗
    """
    # Limpia: solo letras, minúsculas, sin espacios
    limpio = ''.join(char.lower() for char in texto if char.isalpha())
    # Compara con su inversa
    return limpio == limpio[::-1]


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    
    Lógica:
    1. Divide el texto por espacios
    2. Capitaliza cada palabra (.capitalize() = primera mayúscula + resto minúsculas)
    3. Vuelve a unir
    
    Ejemplos:
    - capitalizar_palabras("hola mundo") → "Hola Mundo"
    """
    return ' '.join(palabra.capitalize() for palabra in texto.split())


def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u).
    No distingue mayúsculas/minúsculas.
    
    Lógica:
    1. Define las vocales (mayúsculas + minúsculas)
    2. Cuenta cuántos caracteres del texto están en vocales
    3. Retorna el conteo
    
    Ejemplos:
    - contar_vocales("hola mundo") → o, a, u, o = 4
    - contar_vocales("AEIOU") → A, E, I, O, U = 5
    """
    vocales = "aeiouAEIOU"
    return sum(1 for char in texto if char in vocales)


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César con desplazamiento dado.
    
    ENFOQUE: Matemáticas ASCII (ord/chr) - EDUCATIVO
    
    Lógica:
    1. Para cada carácter:
       - Si es letra minúscula: desplaza dentro de a-z (con wrap)
       - Si es letra mayúscula: desplaza dentro de A-Z (con wrap)
       - Si NO es letra: mantiene igual
    2. El módulo (%) hace que z+1 = a (wrap around)
    
    Ejemplo paso a paso: caesar_cipher("xyz", 1)
    ────────────────────────────────────────
    x: ord('x')=120, (120-97+1)%26=0, chr(0+97)='y'
    y: ord('y')=121, (121-97+1)%26=1, chr(1+97)='z'
    z: ord('z')=122, (122-97+1)%26=0, chr(0+97)='a' ← WRAP!
    Resultado: "yza" ✓
    """
    resultado = ""
    for char in texto:
        if 'a' <= char <= 'z':
            # Rango minúsculas: 0-25
            nuevo = chr((ord(char) - ord('a') + desplazamiento) % 26 + ord('a'))
            resultado += nuevo
        elif 'A' <= char <= 'Z':
            # Rango mayúsculas: 0-25
            nuevo = chr((ord(char) - ord('A') + desplazamiento) % 26 + ord('A'))
            resultado += nuevo
        else:
            # Otros caracteres (espacios, puntuación) no cambian
            resultado += char
    return resultado
