"""
markov1
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

class Agent:
    def __init__(self, pattern=r'\w+|[^\w\s]'):
        self.tensors = {}
        self.pattern = pattern

    def divide(self, code):
        import re
        return re.findall(self.pattern, code)

    def import_(self, file):
        import json
        with open(file, "r", encoding="utf-8") as f:
            self.tensors = json.load(f)

    def save(self, file):
        import json
        with open(file, "w", encoding="utf-8") as f:
            json.dump(
                self.tensors,
                f,
                indent=4,
                ensure_ascii=False
            )

    def train(self, file, type="file"):
        if type == "file":
            lolcode = open(file, "r", encoding="utf-8").read()
        elif type == "text":
            lolcode = file
        tokens = self.divide(
            lolcode
        )
        if "" not in self.tensors:
            self.tensors[""] = []

        self.tensors[""].append(tokens[0])

        if tokens[-1] not in self.tensors:
            self.tensors[tokens[-1]] = []

        self.tensors[tokens[-1]].append(None)

        for num in range(len(tokens)-1):
            token = tokens[num]
            # No evitar duplicados para que las palabras más comunes sean más probables
            if token not in self.tensors:
                self.tensors[token] = [tokens[num+1]]
            else:
                self.tensors[token].append(tokens[num+1])

    def generate(self, toks=-1, seed=""):
        from random import choice
        words = []
        word = seed
        n = 0
        while True:
            try:
                words.append(word)

                word = choice(self.tensors[word])
                if word == None:
                    break
                n += 1
                if n == toks:
                    break
            except (KeyError, IndexError):
                break
        return " ".join(words)
