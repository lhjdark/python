with open('data.txt', 'r') as file:
    print(file.read())
    file.seek(0)
    print(file.readlines())
    file.seek(0)
    print(file.read(1), file.read(8))

    file.seek(0)
    for line in file.readlines():
        print(line, end='')

    file.seek(0)
    for line in file:
        print(line, end='')
    print('----------------')
    file.seek(0)
    print(list(file))
