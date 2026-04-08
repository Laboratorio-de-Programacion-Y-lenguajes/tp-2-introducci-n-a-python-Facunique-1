# ============================================================
# MÓDULO 2: Condicionales
# ============================================================


def clasificar_numero(n: int) -> str:
    """
    Retorna "positivo", "negativo" o "cero" según corresponda.
    
    LÓGICA (tu respuesta 2):
    - Usa operador ternario anidado
    - Si n > 0 → "positivo"
    - Si n < 0 → "negativo"
    - Si no es ninguno → "cero"
    """
    return "positivo" if n > 0 else "negativo" if n < 0 else "cero"


def mayor_de_tres(a: int, b: int, c: int) -> int:
    """
    Retorna el mayor de tres números.
    """
    return max(a, b, c)


def clasificar_nota(nota: float) -> str:
    """
    Retorna la categoría de la nota:
    - nota >= 9: "Sobresaliente"
    - nota >= 7: "Bueno"
    - nota >= 6: "Aprobado"
    - nota < 6:  "Desaprobado"
    """
    if nota >= 9:
        return "Sobresaliente"
    elif nota >= 7:
        return "Bueno"
    elif nota >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"


def es_bisiesto(anio: int) -> bool:
    """
    Retorna True si el año es bisiesto.
    
    LÓGICA (tu respuesta 3):
    - Regla 1: (divisible por 4 AND NO divisible por 100)
    - SE COMBINA CON OR con la Regla 2
    - Regla 2: (divisible por 400)
    
    Ejemplos:
    - 2024: divisible por 4, NO por 100 → True ✓
    - 2000: divisible por 400 → True ✓
    - 1900: divisible por 100, NO por 400 → False ✗
    - 2023: NO divisible por 4 → False ✗
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
