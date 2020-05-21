import sys
sys.path.append('/Users/Rumle/Documents/DAT4/dataScience/realPython/dat4sem2020spring-python/Handins/Assignment02')
from utils import *
import getopt

def usage():
    return """
        -wfn <filetowriteto> <path> writeFileNames(arg1, arg2)
        -wfntr writeFileNamesRecursively(arg1, arg2)
        -rfw readFirstWord(arg1)
        -fe findEmail(arg1)
        -fh findheadlines(arg1)
              
           """


def run(arguments):
    try:
        opts, args = getopt.getopt(arguments, "ho:v", ["help", "path=", "file=" ])

    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    output = None
    verbose = False
    path = ''
    for option, argument in opts:
            if option == "-v":
                verbose = True
            elif option in ("-wfn", "--path"):
                path = argument
            elif option in ("-f", "--file"):
                f = open(argument, 'w')
                f.write(path)
            elif option in ("-h", "--help"):
                print(usage())
                print(arguments)
                sys.exit()

if __name__ == '__main__':
    run(sys.argv[1:])