fruit = 'banana'
index = 0
while index < len(fruit): 
    letter = fruit[index]
    print(index, letter)
    index = index + 1

for index, letter in enumerate(fruit):
    print(index, letter)