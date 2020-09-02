with open('data.txt', 'w') as file:
    try:
        file.write("hello file world!11111\n")
        file.write('Bye file world\n')

    finally:
        file.close()

with open('data.txt', 'r') as myFile:
    try:
        lines = myFile.readlines()
        for line in lines:
            print(line, end=' ')

    finally:
        myFile.close()





