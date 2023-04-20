import pathlib
path = str(pathlib.Path(__file__).parent.absolute())

# Write a program that reads a file and prints only those lines that contain the substring pass as arguments

def read_lines(substring):
    fhand = open(path +"/solutions/text.txt")
    result = ""
    for line in fhand:
        if substring in line:
            result += line
    print(result)
    fhand.close()

read_lines("hola")
read_lines("en")


# Write a program that reads a text file and produces an output file which is a copy of the file, except the first 
# five columns of each line contain a four digit line number, followed by a space, and followed with the full line.

def format_file():
    fhand = open(path + "/solutions/text.txt")
    fresult = open(path + "/solutions/text2.txt", 'w')
    count = 0
    for line in fhand:
        count_str = str(count)
        while len(count_str) < 4:
            count_str = "0" + count_str
        fresult.write(count_str + " " + line)
        count += 1
    fhand.close()
    fresult.close()
    
format_file()


# Write a program that undoes the numbering of the previous excercise: it should read a file with numbered lines and produce another file without line numbers.

def format_file2():
    fhand = open(path + "/solutions/text2.txt")
    fresult = open(path + "/solutions/text3.txt", 'w')
    for line in fhand:
        fresult.write(line[5:])
    
    fhand.close()
    fresult.close()

format_file2()