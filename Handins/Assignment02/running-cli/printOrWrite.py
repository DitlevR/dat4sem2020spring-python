import sys
import csv
import getopt


def doFile(arguments):
    try:
        opts, args = getopt.getopt(arguments, "f", ["file"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    for options, file in opts:
        print(option)
        with open(file) as fObj:
            if option in ("-f", "--file"):
                with open(file) as fObj:
                    for element in list:
                        fObj.write(str(element))
            else:
                reader = csv.reader(fObj)
                for row in reader:
                    print(str(row))


# parser.add_argument("--arg", help="")

if __name__ == '__main__':
    doFile(sys.argv[1])
    # writeToFile(sys.argv[1], sys.argv[2])
    # writeManyToFile(sys.argv[1])
    # listFile(sys.argv[1])parser.add_argument('--text', default='', help='What do you want to write')
