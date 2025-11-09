import os

try:
    with open("sample.txt", "rt") as fh:
        print(fh.read())
except:
    print("The file 'sample.txt' does not exist")

