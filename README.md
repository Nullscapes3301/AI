# AI

Esta "AI" es una aplicacion independiente de las cadenas de Markov de primer orden.

## Compatibilidad

* Python 3.14.7 o compatible

## Contactos

* [contactwithnull@gmail.com](mailto:contactwithnull@gmail.com)

## Como usar

Dentro de *markov1.py* hay una clase `Agent`. Esta sirve para crear un agente.
Dentro de \_\_init__ puedes especificar **pattern** para separar los tokens de entrenamiendo, por defecto es este:

```regex
\w+|[^\w\s]
```

Para entrenarla se usa el atributo `train` que recibe un argumento normal y uno opcional, el normal puede ser o texto de entrenamiento o un archivo, si el segundo argumento se pone como `text` se tratara el otro como texto de entrenamiento, si el segundo se pone como `file` o no se pone entonces el primero sera tratado como el archivo a abrir.
Puedes entrenarlo todas las veces que quieras y solo se añadiran tokens nuevos o se sobreescribiran los ya existentes, nunca se borraran.
Una vez ya se haya entrenado puedes guardarlo son `save` en el que especificas la ruta del archivo.
Si ya tienes una AI guarada en un *.json* entonces puedes importarla con `import_`.
El entrenamiento se guarda en el atributo `tensors` que podria guardar algo como

```json
{
    "": [
        "Hello"
    ],
    ".": [
        null,
        "Hello"
    ],
    "Hello": [
        "world",
        "Pedro"
    ],
    "world": [
        "."
    ],
    "Pedro": [
        "."
    ]
}
```

El token **""** (string vacio) es el primer token encontrado en cada entrenamiento, **null** se pone en los tokens que representan el final y si se elije se terminara inmediatamente la generacion de texto.

Para generar texto se usa el atributo `generate` que siempre retorna un string que puedes espeficidar dos argumentos, `toks` y `seed`,
toks representa la cantidad maxima de palabras que quieres que genere, por ejemplo con **toks=100** generara 100 palabras si no encuentra un *null* antes, por defecto es -1 asi que si no lo especificas solo terminara cuando encuentre un *null*. seed es la primera palabra que se generar, por defecto es "" (un string vacio) que es el primer token encontrado asi que en el ejemplo anterior pones **seed="Pedro"** entonces la primer palabra que se usara para generar el texto sera Pedro. generate funciona muy simple, agarra el token actual y de los tensores agarra la lista correspondiente, agarra aleatoriamente un token de la lista, lo agrega al resultado y lo pone como palabra actual, repite el proseso hasta que algo lo termine y al final junta todo el texto generado y lo retorna.

```python
pedro = Agent()
laura = Agent()
mateo = Agent()

pedro.train("Hola mundo", "text")
laura.train("texto.txt")
mateo.import_("tensores.json")

print(pedro.generate())
print(laura.generate(toks=100))
print(mateo.generate(seed="El"))
```
