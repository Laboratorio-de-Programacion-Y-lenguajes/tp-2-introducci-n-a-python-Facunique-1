# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

[Herramienta]: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

###### Aclaración:
Utilicé Gemini para que haga el prompt que sería enviado para la resolución de cada módulo a Claude Haiku del chat de VSCode, en Gemini cargué el paper de Promt Engeneering y las sentencias que se dictaban en el código de cada módulo.


## Mis prompts

### 1 - variables.py

Claude Haiku integrado a VSCode: 

**Prompt usado**:
> Actuá como un tutor de Python. Dame una receta paso a paso para implementar estas funciones: crear_saludo usando f-strings, suma_enteros, es_mayor_de_edad, una que devuelva el nombre del tipo de dato (__name__) y otra que convierta strings a float.

**Resultado obtenido**:
Receta paso a paso para implementar las funciones 🐍
Perfecto, te ayudaré como tutor. Aquí está la guía completa para cada función:

1. crear_saludo (usando f-strings)

Paso a paso:

def crear_saludo(nombre: str) -> str:
    # 1. Usa el prefijo 'f' antes de las comillas
    # 2. Coloca variables entre { }
    # 3. Python reemplaza el contenido de { } con el valor
    return f"Hola, {nombre}!"

y así para el punto 2.,3.,4. y 5.

**¿Lo usaste tal cual o lo modificaste?**
Las use tal cual porque estaban bien hechas, tenian logica y fueron corroboradas las funciones que no sabia que hacian.

---

### 2 - condicionales.py

Claude Haiku integrado a VSCode: 

**Prompt usado**:
> Quiero implementar las funciones de condicionales.py. Actuá bajo el patrón de Interacción Invertida: haceme preguntas sobre cómo priorizar las condiciones de las notas, cómo manejar el cero en la clasificación y qué reglas aplicar para los años bisiestos. Una vez que te responda, generá el código final.

**Resultado obtenido**:

Pregunta 1: Clasificación de Notas
El docstring dice que tenemos 4 categorías según el rango de la nota. Si tuvieras que implementar esto con if/elif/else:

¿En qué orden verificarías las condiciones? (¿empezar por 9, por 6, o por otro lado?)
¿Por qué ese orden es mejor que otro?

Pregunta 2: Clasificar Número
Para devolver "positivo", "negativo" o "cero" según el valor:

¿Cómo manejarías el cero? (¿es positivo, negativo, o su propio caso?)
¿Podrías hacerlo con operadores ternarios (if/else en una línea) o prefieres un if/elif/else tradicional?

Pregunta 3: Años Bisiestos
"Un año es bisiesto si es divisible por 4, excepto los divisibles por 100, salvo que también lo sean por 400."

¿Cómo expresarías esta regla con and/or?
¿Cuál es el orden lógico que tiene más sentido:
(divisible por 4 AND no divisible por 100) OR (divisible por 400)
Otra forma?

Mis respuestas:

respuesta 1:

- Verifico en orden descendente empezando por 9
- Es lo midmo descendente que ascendente, tienen las misma cantidad de if

respuesta 2:

- El cero tiene su propio caso "cero"
- Prefiero una version ternaria

respuesta 3:

- Lo expresaría con or
- El orden lógico que tiene sentido es: (divisible por 4 AND no divisible por 100) OR (divisible por 400)

**¿Lo usaste tal cual o lo modificaste?**
Las use tal cual porque estaban bien hechas, tenian logica.

---

### 3 - listas.py

Claude Haiku integrado a VSCode: 

**Prompt usado**:
> Necesito implementar funciones para manipular listas (suma, filtro de pares, inversión, eliminación de duplicados y aplanado). Utiliza el patrón Verificador Cognitivo: antes de darme el código, generá preguntas que me ayuden a identificar casos borde, como qué hacer con listas vacías o listas con tipos de datos mezclados.

**Resultado obtenido**:
erificador Cognitivo: Preguntas sobre Casos Borde
Caso 1: suma_lista() con lista vacía
¿Debería retornar 0, None, o lanzar un error?
¿Por qué esa sería la respuesta más lógica?

Caso 2: filtrar_pares() con lista vacía
¿Debería retornar una lista vacía [] o algo diferente?
Si hay pares, ¿preserva el orden original?

Caso 3: invertir_lista() con un elemento
¿Qué hace con una lista de un único elemento?
¿Y con listas ya invertidas?

Caso 4: eliminar_duplicados() con tipos mezclados
¿1 (int) y "1" (string) son duplicados o diferentes?
¿Mantiene el orden de primera aparición?

Caso 5: aplanar_lista() con anidamiento profundo
¿Debería aplanar TODOS los niveles o solo un nivel?
¿Qué pasa si hay strings: [["hola"], ["mundo"]]?

Caso 6: suma_lista() con tipos mezclados
¿Debería convertir strings a números o lanzar error?
¿Qué tipos son válidos: int, float, ambos?


Mi respuesta:
caso 1: la lista vacía debería retornar 0, porque las respuestas son números, y 0 es el vacío en los números.

caso 2: la lista de pares vacía debe retornar una lista vacía; si hay pares deben preservar el orden.

caso 3: con un único elemento, y se devulven listas invertidas, no se reconoce si ya estaban invertidas o no.

caso 4: 1 y "1" son diferentes, ya que son de distinto tipo y prevalece el orden.

caso 5: debería aplanar todos los niveles, se aplanan en todos los casos.

caso 6: solo se admiten elementos del tipo int y floats


Luego me pasó todo el código requerido según las especificaciones de los casos borde que le pasé.

**¿Lo usaste tal cual o lo modificaste?**
Las use tal cual porque estaban bien hechas, tenian logica y las corrobore.

---

### 4 - diccionarios.py

Claude Haiku integrado a VSCode: 

**Prompt usado**:
> Usando el patrón de Generación Infinita, dame 2 ejemplos de diccionarios con las claves: nombre, apellido, edad y mail. Después, escribí las funciones contar_palabras, invertir diccionario, merge_diccionarios (si hay claves repetidas prevalecen d2) y filtrar_por_valor

**Resultado obtenido**:
La IA me paso el código y ejemplos de cada una de las funciones explicando que hace cada parte.

**¿Lo usaste tal cual o lo modificaste?**
Las use tal cual porque estaban bien hechas, los comentarios y ejemplos sirvieron para entender el código.

---

### 5 - loops.py

GitHub Copilot: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 6 - funciones.py

GitHub Copilot: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 7 - operaciones.py

GitHub Copilot: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
    
