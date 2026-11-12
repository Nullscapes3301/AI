# Modelo neuronal

Este es un pequeño modelo neuronal real(no como el de Markov).

## Requisitos

### Uso

* python 3.14 o compatible

## Modo de uso

Para usar este modulo nesesitas usar la clase Neuron del modulo y poner los dos argumentos `pesos` y `umbral`, pesos es una lista de numeros o decimales del modulo decimal de Python, la formula para calcular el retorno lo que hace es basicamente esto:

```text
(w1)(i1)+(w2)(i2)+...(wn)(in)
```

y si el resultado es *superior o igual* al numero o decimal del `umbral`, si es inferior retorna 0. Mientras mas alto sea el index mas avanzada es la capa, cada capa recibe una lista con todos los resultados de la capa anterior. Si la lingitud de `peso` no es igual a la lista recibida como prompt. Pero... como mandarle prompt? Simple, llamas a la instancia y pones el prompt como una lista de numeros o decimales. Para crear un modelo se crea una lista con listas con intsancias de la clase `Neuron`. La primera capa de neuronas recibe el prompt como prompt. La clase retorna una lista de numeros o decimales con los resultados de la ultima capa de neuronas. Para generar se usa la funcion `generate` que recibe dos argumentos, el primero es la lista que contiene las capas y neuronas del modelo, seguido de una lista de numeros o decimales que se pasara a la primera capa como prompt.
Por ejemplo:

```python
_gate = [
        [
            Neuron(pesos=[0.5, 0.5], umbral=1)
        ],
    ]

prompts = [
    [ 0 , 0 ],
    [ 0 , 1 ],
    [ 1 , 0 ],
    [ 1 , 1 ],
]

for i in prompts:
    print(
        f"prompt {i} returns:",
        generate(
            _gate,
            i
        )[0]
    )
```

Imprime:

```text
prompt [0, 0] returns: 0
prompt [0, 1] returns: 0
prompt [1, 0] returns: 0
prompt [1, 1] returns: 1.0
```
