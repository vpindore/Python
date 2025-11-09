import os

try:
    with open("output.txt", "wt") as fh:
        line = input("Enter text to write to file: ")
        fh.write(line)
        fh.write("\n")
    with open("output.txt", "at") as fh:
        line = input("Enter addtional text to append: ")
        fh.write(line)
    with open("output.txt", "rt") as fh:
        print("Final content of output.txt:\n")
        print(fh.read())

except:
    print("File sample.txt does not exist")

