cadenas = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go", "Swift"]
caracter = "y"

char_with_y = list(filter(lambda x: caracter in x, cadenas))
print(f"Cadenas con '{caracter}': {char_with_y}")
