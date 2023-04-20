"""
Write a function that mirrors its argument:

assert(mirror("good") == "gooddoog")
assert(mirror("Python") == "PythonnohtyP")
assert(mirror("") == "")
assert(mirror("a") == "aa")
"""

def mirror(phrase):
    return phrase + phrase[::-1]

print(mirror("good"))
print(mirror("Python"))
print(mirror(""))
print(mirror("a"))



"""
Write a function that removes all occurrences of a given letter from a string:

assert(remove_letter("a", "apple") == "pple")
assert(remove_letter("a", "banana") == "bnn")
assert(remove_letter("z", "banana") == "banana")
assert(remove_letter("i", "Mississippi") == "Msssspp")
assert(remove_letter("b", "") == "")
assert(remove_letter("b", "c") == "c")
"""

def remove_letter(letter, phrase):
    return phrase.replace(letter, "")

print(remove_letter("a", "apple"))
print(remove_letter("a", "banana"))
print(remove_letter("z", "banana"))
print(remove_letter("i", "Mississippi"))
print(remove_letter("b", ""))
print(remove_letter("b", "c"))



"""
Encapsule in a function named count_letters, and generalize it so that it accepts the string and the letter as arguments. 
Make the function return the number of characters, rather than print the answer. The caller should do the printing.

fruit = "banana"
count = 0
for char in fruit:
    if char == "a":
        count += 1
print(count)
"""

def count_letters(letter, phrase):
    # OPCIÓN 1.
    # return phrase.count(letter)

    count = 0
    for char in phrase:
        if char == letter:
            count += 1
    return count



"""
Assign to a variable in your program a triple-quoted string that contains your favourite paragraph of text — perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.
Write a function which removes all punctuation from the string, breaks the string into a list of words, and counts the number of words in your text that contain the letter “e”. 
Your program should print an analysis of the text like this:
Your text contains 243 words, of which 109 (44.8%) contain an "e".
"""

def paragraph_analysis(paragraph):
    words = paragraph.replace(".", "").replace(",", "").replace(":", "").replace(";", "").split()
    words_with_e = 0
    for word in words:
        if 'e' in word:
            words_with_e += 1

    percentage = words_with_e / len(words) * 100
    percentage = '{:.2f}'.format(percentage)
    print(f"Your text contains {len(words)} words, of which {words_with_e} ({percentage}%) contain an \"e\".")

example = """
En un lugar de la Mancha, de cuyo nombre no quiero 
acordarme, no ha mucho tiempo que vivía un hidalgo de los de 
lanza en astillero, adarga antigua, rocín flaco y galgo corredor. 
Una olla de algo más vaca que carnero, salpicón las más noches, 
duelos y quebrantos los sábados, lantejas los viernes, algún 
palomino de añadidura los domingos, consumían las tres partes 
de su hacienda
"""
paragraph_analysis(example)