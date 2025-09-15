from random import randint

"""
Muitas funções foram inspiradas no BOT do Discord rollem

4d6 -- soma de 4 dados de 6 lados
4#d6 -- 4 rolagens de 1d6

4d6dl1 -- pega o menor e retira da soma

4d6dh1  -- pega o maior e retira da soma 

6#4d6 -- 6 rolagens de 4d6
"""

"""
Simula a rolagem de 'x' dados de 'y' lados.

Args:
    x (int): O número de dados a serem rolados.
    y (int): O número de lados de cada dado.

Returns:
    list: Uma lista de inteiros com os resultados de cada dado.
"""

def roll_XdY(x, y):
    return list((randint(1, y)) for _ in range(x))

# drop the Z lowest result
def roll_XdYdl_Z(x, y, z):
    rolls_sort = sorted(roll_XdY(x, y))
    for _ in range(z):
        rolls_sort.pop(0)
    return rolls_sort

def roll_XdYdh_Z(x, y, z):
    rolls_sort = sorted(roll_XdY(x, y), reverse=True)
    for _ in range(z):
        rolls_sort.pop(0)
    return rolls_sort
