# ============================================================
# MÓDULO 5: Loops
# ============================================================


def contar_hasta(n: int) -> list:
    """
    Retorna una lista con los números del 1 al n (inclusive).
    
    TUS DECISIONES:
    - Si n < 1 → retorna lista vacía []
    - Usa range() que es más eficiente que un loop manual
    
    Ejemplos:
    - contar_hasta(5) → [1, 2, 3, 4, 5]
    - contar_hasta(0) → []
    - contar_hasta(-3) → []
    """
    if n < 1:
        return []
    return list(range(1, n + 1))


def tabla_multiplicar(n: int) -> list:
    """
    Retorna una lista con los primeros 10 múltiplos de n.
    
    TUS DECISIONES:
    - Siempre genera exactamente 10 múltiplos
    - Usa list comprehension para eficiencia
    
    Ejemplos:
    - tabla_multiplicar(3) → [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    - tabla_multiplicar(5) → [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    """
    return [n * i for i in range(1, 11)]


def suma_digitos(n: int) -> int:
    """
    Retorna la suma de los dígitos de un número entero.
    
    TUS DECISIONES:
    - Suma SOLO los dígitos (ignora el signo negativo)
    - Usa abs() para trabajar con valor absoluto
    - Convierte cada dígito a int y suma
    
    Ejemplos:
    - suma_digitos(123) → 1 + 2 + 3 = 6
    - suma_digitos(-123) → suma de 1, 2, 3 = 6 (ignora el -)
    - suma_digitos(0) → 0
    """
    return sum(int(digito) for digito in str(abs(n)))


def es_primo(n: int) -> bool:
    """
    Retorna True si n es un número primo.
    
    TUS DECISIONES:
    - Usa optimización con sqrt (raíz cuadrada)
    - Porque: si n = a * b, uno de a o b SIEMPRE es <= √n
    - Esto reduce complejidad de O(n) a O(√n)
    
    Ejemplos:
    - es_primo(17) → True (no divisible por 2, 3, 4)
    - es_primo(1) → False (por definición)
    - es_primo(4) → False (4 % 2 == 0)
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> list:
    """
    Retorna los primeros n números de la serie de Fibonacci (versión iterativa).
    
    TUS DECISIONES:
    - Retorna [] si n <= 0 (casos base inválidos)
    - VERSIÓN ITERATIVA (no recursiva) para mejor rendimiento
    - Construcción manual de la serie evita recursión lenta
    
    Matemática:
    - F(0) = 0
    - F(1) = 1
    - F(n) = F(n-1) + F(n-2)
    
    Ejemplos:
    - fibonacci(6) → [0, 1, 1, 2, 3, 5]
    - fibonacci(1) → [0]
    - fibonacci(0) → []
    - fibonacci(-5) → []
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Versión iterativa: construye la serie paso a paso
    fib = [0, 1]
    for i in range(2, n):
        siguiente = fib[i - 1] + fib[i - 2]
        fib.append(siguiente)
    return fib
