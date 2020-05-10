import sys
import csv
import getopt



def usage():
    return """
    
              Usage : printOrWrite.py -p <csvpath> or printOrWrite.py --path <csvpath>
              printOrWrite.py -f <filename> or printOrWrite.py --file <filename>
              
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
            elif option in ("-p", "--path"):
                path = argument
            elif option in ("-f", "--file"):
                f = open(argument, 'w')
                f.write(path)
                        
                    

            elif option in ("-h", "--help"):
                print(usage())
                print(arguments)
                sys.exit()
                

            

            

# parser.add_argument("--arg", help="")

if __name__ == '__main__':
    run(sys.argv[1:])

    #writeToFile(sys.argv[1], sys.argv[2])
    # writeManyToFile(sys.argv[1])
    # listFile(sys.argv[1])parser.add_argument('--text', default='', help='What do you want to write')
