import sys
import argparse
from os import listdir
import os
import re


def writeFileNames(arg1, arg2):
    with open(arg2, 'a') as a:
        for x in listdir(arg1):
            a.write(x)


def writeFileNamesRecursively(arg1, arg2):
    with open(arg2, 'a') as a:
        for subdir, dirs, files in os.walk(arg1):
            for file in files:
                filepath = subdir + os.sep + file
                a.write(str(filepath))


def readFirstWord(arg1):
    for x in listdir(arg1):
        with open(x, ) as a:
            line = a.readline()
            firstLine = line[0:10]
            print(firstLine)


def findEmail(arg1):
    for x in listdir(arg1):
        for n in open(x, 'r'):
            email = re.findall('\S+@\S+', n)
            if(email != None):
                print(email)


def findheadlines(arg1):
    for x in listdir(arg1):
        with open(x, 'r') as a:
            for line in a:
                if line.startswith('#'):
                    print(line)


if __name__ == '__main__':
    # writeFileNamesRecursively(sys.argv[1], sys.argv[2])
    # readFirstWord(sys.argv[1])
    findheadlines(sys.argv[1])
