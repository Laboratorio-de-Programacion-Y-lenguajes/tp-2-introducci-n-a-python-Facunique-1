# ============================================================
# MÓDULO 1: Variables y Tipos de Datos
# ============================================================
# Completá cada función siguiendo las instrucciones.
# NO modifiques los nombres de las funciones ni sus parámetros.
# ============================================================


def crear_saludo(nombre: str) -> str:
    """
    Retorna un saludo personalizado.
    Ejemplo: crear_saludo("Ana") -> "Hola, Ana!"
    """
    # 1. Usa el prefijo 'f' antes de las comillas
    # 2. Coloca variables entre { }
    # 3. Python reemplaza el contenido de { } con el valor
    return f"Hola, {nombre}!"
    


def suma_enteros(a: int, b: int) -> int:
    """
    Retorna la suma de dos enteros.
    """
    # 1. Recibe dos parámetros de tipo int
    # 2. Suma ambos con el operador +
    # 3. Retorna el resultado
    return a + b


def es_mayor_de_edad(edad: int) -> bool:
    """
    Retorna True si edad >= 18, False caso contrario.
    """
    # 1. Compara si edad es >= 18
    # 2. Si es verdadero, retorna True
    # 3. Si es falso, retorna False
    return edad >= 18
    


def tipo_de_dato(valor) -> str:
    """
    Retorna el nombre del tipo de dato del valor recibido.
    Ejemplo: tipo_de_dato(42) -> "int"
             tipo_de_dato("hola") -> "str"
    """
    # 1. Obtiene el tipo del valor con type()
    # 2. Accede al nombre del tipo con __name__
    # 3. Retorna el nombre del tipo
    return type(valor).__name__
    


def convertir_a_float(valor: str) -> float:
    """
    Convierte un string numérico a float.
    Ejemplo: convertir_a_float("3.14") -> 3.14
    """
    # 1. Recibe un string numérico
    # 2. Convierte a float con float()
    # 3. Retorna el resultado
    return float(valor)
    
