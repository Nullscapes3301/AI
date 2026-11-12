"""
Simple neuronal model
Copyright (C) 2026 Nullscapes

Repository: https://github.com/Nullscapes3301/AI/

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from decimal import Decimal as dec

__all__ = ["Neuron", "generate"]

class Neuron:
    def __init__(self, pesos, umbral):
        if isinstance(pesos, list):
            tmp = []
            for i in pesos:
                tmp.append(dec(str(i)))
            pesos = tmp
        else:
            raise TypeError("Los pesos deben ser una lista")
        if not isinstance(umbral, (int, dec)):
            raise TypeError("El umbral debe ser un numero")
        self.pesos = pesos
        self.umbral = umbral

    def __call__(self, entradas):
        if isinstance(entradas, (tuple, list)):
            pass
        else:
            raise TypeError("Las entradas deben ser una lista")
        if len(entradas) != len(self.pesos):
            raise ValueError(
                f"Entradas: {len(entradas)}, "
                f"Pesos: {len(self.pesos)}, "
                f"Entradas recibidas: {entradas}"
            )
        resultado = 0
        for n in range(len(entradas)):
            entrada = entradas[n]
            peso = self.pesos[n]
            resultado += peso*entrada
        if resultado >= self.umbral:
            salida = resultado
        else:
            salida = 0
        return salida

def generate(red_n, inputs):

    output = list(inputs)

    for capa in red_n:
        next_output = []

        for neurona in capa:
            next_output.append(neurona(output))

        output = next_output

    return output

if __name__ == "__main__":
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