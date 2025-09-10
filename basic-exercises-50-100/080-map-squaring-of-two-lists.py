def suma_cuadrados(a, b):
    return (a + b) ** 2


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [9, 8, 7, 6, 5, 4, 3, 2]

result = list(map(suma_cuadrados, list1, list2))
print(result)
