"""
Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. 
Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
"""

import pathlib
import re
path = str(pathlib.Path(__file__).parent.absolute())

expresion = input("Introduce una expresion regular: ")

def read_lines(expresion):
    try:
        fhand = open(path +"/mbox.txt")
        try:
            count = 0
            lista = []
            for line in fhand:
                if len(re.findall(expresion, line)) != 0:
                    count += 1
                    lista.append(line)
            print(lista)
            return f"mbox.txt had {count} that matched {expresion}"
        except re.error:
            print('The pattern is not valid')
    except FileNotFoundError:
        print('File mbox.txt not found')
print(read_lines(expresion))


"""
Exercise 2: Write a program to look for lines of the form:
New Revision: 39772

Extract the number from each of the lines using a regular expression and the findall() method. 
Compute the average of the numbers and print out the average as an integer.
Enter file:mbox.txt
38549
Enter file:mbox-short.txt
39756
"""

def read_lines():
    fhand = open(path +"/mbox.txt")
    lista = []
    for line in fhand:
        line = line.rstrip()
        if (len(re.findall(r'^New\sRevision:\s[0-9]+', line)) != 0):
            lista.append(line)
    return lista, len(lista)

print(read_lines())


def read_lines_v2():
    fhand = open(path +"/mbox.txt")
    lista = []
    for line in fhand:
        line = line.rstrip()
        expresion = r'^New\sRevision:\s([0-9]+)'
        lista_2 = re.findall(expresion, line)
        if len(lista_2) != 0:
            for element in lista_2:
                lista.append(element)
    total_sum = 0
    for number in lista:
        total_sum+= int(number)
    print(total_sum / len(lista))
    return lista

print(read_lines_v2())
