"""
* Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored. A sample output of the program when the user enters the data “ThiS is String with Upper and lower case Letters”, would look this this:
  | letter | count  |
  |---|----:|
  | a | 2  |
  | c | 1  |
  | d | 1 |
  | e | 5 |
  | g | 1 |
  | h | 2 |
  | i | 4 |
  | l | 2 |
  | n | 2 |
  | o | 1 |
  | p | 2 |
  | r | 4 |
  | s | 5 |
  | t | 5 |
  | u | 1 |
  | w | 2 |

"""

def contar_palabras(texto):
    diccionario = {}
    palabras = texto.lower().split()
    for palabra in palabras:
        for letra in palabra:
            if letra not in diccionario:
                diccionario[letra] = 1
            else:
                diccionario[letra] = diccionario[letra] + 1
    letras_ordenadas = sorted(diccionario.keys())
    resultado = {}
    for letra in letras_ordenadas:
        resultado[letra] = diccionario[letra]
    print(diccionario)
    print(resultado)

string = "zturslfjeispqmefosdl"
contar_palabras(string)