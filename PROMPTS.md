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
📋 Preguntas para tu análisis:
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
Respondé estas tres preguntas y te genero el código completo comentado con la lógica que decidamos juntos. 🎯

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
> 

**Resultado obtenido**:

**¿Lo usaste tal cual o lo modificaste?**
Las use tal cual porque estaban bien hechas, tenian logica y las corrobore.

---

### 4 - diccionarios.py

GitHub Copilot: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


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
    
