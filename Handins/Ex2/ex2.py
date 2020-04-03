import webget

url = 'https://raw.githubusercontent.com/ehmatthes/pcc/master/chapter_10/pi_30_digits.txt'
webget.dowload(url)



def print_file_content(file):
    with open('pi_30_digits.txt') as file_object:
        contents = file_object.read()
print(contents)

