import os
import random

class Characters:

    def non_ascii(num=5):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/characters.txt', 'r', encoding="utf8") as file:
            data = file.read()
        return "".join(random.choices(data, k=num))
