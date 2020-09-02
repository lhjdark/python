with open('data.txt', 'r') as file:     # read str
    print(file.read())
    file.close()

with open('data.txt', 'rb') as file:    #read byte--unicode
    print(file.read())
