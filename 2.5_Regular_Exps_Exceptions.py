"""
8th Linux Festival, Python Workshop
By Sina Baharlouie, Sajad Azami
May 2016
"""


# Exceptions are key method for handling errors in Python
def main():
    # try:
    #     fh = open("xdata.txt")
    # except:
    #     print ("could not open file")
    # else:
    #     for i in fh:
    #         print (i)
    #
    # try:
    #     readfile("data.doc")
    # except IOError as e:
    #     print (e)
    # except ValueError as e:
    #     print (e)

    # Regular expressions are good for matching text
    # re a small language
    import re

    fh = readfile("python_wiki.txt")
    for i in fh:
        if re.search('(p|P)ython', i):
            print (i)

    for i in fh:
        print (re.sub('(p|P)ython', "##", i))


def readfile(filename):
    if str(filename).endswith(".txt"):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError("File name is incorrect")


if __name__ == "__main__":
    main()
