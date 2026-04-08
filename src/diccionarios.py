# ============================================================
# MÓDULO 4: Diccionarios
# ============================================================


def contar_palabras(texto: str) -> dict:
    """
    Retorna un diccionario con la frecuencia de cada palabra.
    - Convierte a minúsculas para comparar
    - Divide el texto por espacios
    - Cuenta cuántas veces aparece cada palabra
    
    Ejemplo: contar_palabras("hola mundo hola") → {"hola": 2, "mundo": 1}
    """
    palabras = texto.lower().split()  # Minúsculas y dividir
    frecuencia = {}
    for palabra in palabras:
        # Si existe, suma 1; si no existe, inicia en 1
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia


def invertir_diccionario(d: dict) -> dict:
    """
    Intercambia claves y valores del diccionario.
    
    Ejemplo: invertir_diccionario({"a": 1, "b": 2}) → {1: "a", 2: "b"}
    """
    return {valor: clave for clave, valor in d.items()}


def merge_diccionarios(d1: dict, d2: dict) -> dict:
    """
    Combina dos diccionarios en uno nuevo.
    Si hay claves iguales, d2 sobrescribe d1.
    
    Usa el operador de desempaque ** (unpacking)
    """
    return {**d1, **d2}


def filtrar_por_valor(d: dict, minimo: int) -> dict:
    """
    Retorna un diccionario solo con valores >= minimo.
    
    Usa list comprehension (pero para diccionarios)
    """
    return {clave: valor for clave, valor in d.items() if valor >= minimo}
