# ============================================================
# MÓDULO 6: Funciones
# ============================================================


def aplicar_funcion(lista: list, func) -> list:
    """
    Aplica func a cada elemento de la lista y retorna la nueva lista.
    
    PATRÓN: Map (Mapeo funcional)
    - Transforma cada elemento usando una función
    - No modifica la lista original
    
    Ejemplos:
    - aplicar_funcion([1, 2, 3], lambda x: x * 2) → [2, 4, 6]
    - aplicar_funcion([1, 2, 3], lambda x: x ** 2) → [1, 4, 9]
    """
    return [func(elemento) for elemento in lista]


def componer(f, g):
    """
    Retorna una nueva función que aplica g y luego f.
    
    PATRÓN: Function Composition (Composición de funciones)
    - Matemáticamente: (f ∘ g)(x) = f(g(x))
    - Permite encadenar transformaciones
    - Retorna una FUNCIÓN, no un valor
    
    Ejemplos:
    - h = componer(lambda x: x * 2, lambda x: x + 1)
    - h(5) = (5 + 1) * 2 = 12
    
    - h = componer(str.upper, lambda x: x.strip())
    - h("  hola  ") = "HOLA"
    """
    def funcion_compuesta(x):
        # Primero aplica g, luego aplica f al resultado
        return f(g(x))
    return funcion_compuesta       


def memoizar(func):
    """
    Retorna una versión de func que cachea sus resultados.
    Si se llama con los mismos argumentos, retorna el resultado cacheado.
    
    PATRÓN: Memoization (Memorización / Caché)
    - Almacena resultados previos en un diccionario
    - Si se llama con los mismos argumentos, retorna del caché
    - ENORME mejora de rendimiento en funciones costosas con mismos inputs
    
    Ejemplos:
    - @memoizar
      def fibonacci(n):
          if n <= 1: return n
          return fibonacci(n-1) + fibonacci(n-2)
      
      fibonacci(30) # Primera vez: lento
      fibonacci(30) # Segunda vez: instantáneo (del caché)
    """
    cache = {}
    
    def wrapper(*args):
        # Si ya calculamos esto, retorna del caché
        if args in cache:
            return cache[args]
        
        # Si no, calcula el resultado
        resultado = func(*args)
        
        # Guarda en caché para próximas llamadas
        cache[args] = resultado
        
        return resultado
    
    return wrapper


def reducir(lista: list, func, inicial):
    """
    Aplica func acumulativamente a los elementos de lista,
    comenzando con inicial.
    
    PATRÓN: Reduce (Reducción / Fold)
    - Acumula un valor iterando sobre la lista
    - Combina elemento a elemento con una función
    - Transforma una colección en un ÚNICO valor
    
    Ejemplos:
    - reducir([1, 2, 3], lambda a, b: a + b, 0)
      → ((0 + 1) + 2) + 3 = 6
    
    - reducir([1, 2, 3, 4], lambda a, b: a * b, 1)
      → ((1 * 1) * 2) * 3) * 4 = 24 (factorial)
    
    - reducir(["hola", "mundo"], lambda a, b: a + " " + b, "")
      → "hola mundo"
    """
    acumulador = inicial
    for elemento in lista:
        # Aplica func al acumulador actual y al elemento
        acumulador = func(acumulador, elemento)
    return acumulador