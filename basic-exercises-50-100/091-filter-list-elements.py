lista1 = [1, 2, [3, 4], ["a", "b"], 5, 6]

listas_dentro = list(filter(lambda x: isinstance(x, list), lista1))
print(f"Listas dentro de lista1: {listas_dentro}")
