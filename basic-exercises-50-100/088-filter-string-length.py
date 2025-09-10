'''
Filtra cadenas de lonmgitud mayor a 5 caracteres de una lista
y devuelve una nueva lista con las cadenas filtradas.
'''

cadenas = ["Python", "Java", "C++", "JavaScript", "Go", "Ruby", "React", "Node.js", "HTML", "CSS"]
cadenas_filtradas = list(filter(lambda x: len(x) > 5, cadenas))

print(f"Cadenas filtradas: {cadenas_filtradas}")
