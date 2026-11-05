"""
Nullscapes proyect "markov1"
Copyright (C) 2026 Nullscapes

Repository:  https://github.com/Nullscapes3301/AI/

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
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
