# ============================================================
# MÓDULO 3: Listas
# ============================================================


def suma_lista(numeros: list) -> int | float:
    """
    Retorna la suma de todos los elementos de la lista.
    
    TUS DECISIONES (Caso 6):
    - Solo acepta int y float
    - Lista vacía retorna 0
    - Lanza error si encuentra otro tipo
    
    Ejemplos:
    - suma_lista([1, 2, 3]) → 6
    - suma_lista([1.5, 2.5]) → 4.0
    - suma_lista([]) → 0
    - suma_lista([1, "2"]) → TypeError
    """
    for num in numeros:
        # Excluye bool porque en Python bool es subclase de int
        if isinstance(num, bool) or not isinstance(num, (int, float)):
            raise TypeError(f"Se esperaba int/float, recibido {type(num).__name__}")
    return sum(numeros)


def filtrar_pares(numeros: list) -> list:
    """
    Retorna una nueva lista con solo los números pares.
    
    TUS DECISIONES (Caso 2):
    - Lista vacía retorna lista vacía
    - Preserva el orden original
    
    Ejemplos:
    - filtrar_pares([1, 2, 3, 4]) → [2, 4]
    - filtrar_pares([]) → []
    """
    return [n for n in numeros if n % 2 == 0]


def invertir_lista(lista: list) -> list:
    """
    Retorna la lista invertida SIN modificar la original.
    
    TUS DECISIONES (Caso 3):
    - Un elemento sigue siendo un elemento
    - No hay forma de saber si ya estaba invertida
    
    Ejemplos:
    - invertir_lista([1, 2, 3]) → [3, 2, 1]
    - invertir_lista([42]) → [42]
    """
    return lista[::-1]


def eliminar_duplicados(lista: list) -> list:
    """
    Retorna una nueva lista sin elementos duplicados,
    manteniendo el orden de primera aparición.
    
    TUS DECISIONES (Caso 4):
    - 1 (int) y "1" (string) son DIFERENTES (tipos distintos)
    - Mantiene orden de primera aparición
    
    Ejemplos:
    - eliminar_duplicados([1, 2, 1, 3]) → [1, 2, 3]
    - eliminar_duplicados([1, "1", 1]) → [1, "1"]  (1 e "1" son distintos)
    """
    seen = set()
    result = []
    for item in lista:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def aplanar_lista(lista: list) -> list:
    """
    Dada una lista de listas, retorna todos los elementos en una SOLA lista.
    Aplanar TODOS los niveles de profundidad.
    
    TUS DECISIONES (Caso 5):
    - Aplanar recursivamente TODOS los niveles
    - No solo el primer nivel
    
    Ejemplos:
    - aplanar_lista([[1, 2], [3, 4]]) → [1, 2, 3, 4]
    - aplanar_lista([[[1, 2]], [3, 4]]) → [1, 2, 3, 4]  (TODOS los niveles)
    - aplanar_lista([]) → []
    """
    result = []
    for item in lista:
        if isinstance(item, list):
            # Si es una lista, aplanarla recursivamente
            result.extend(aplanar_lista(item))
        else:
            # Si no es lista, agregar el elemento
            result.append(item)
    return result
