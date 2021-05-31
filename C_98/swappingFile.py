def swapFileData():
    file1 = input("enter file's name 1:- ")
    file2 = input("enter file's name 2:- ")

    with open(file2, 'r') as b:
        data_2 = b.read()
    print(data_2)

    with open(file1, 'r') as a:
        data_1 = a.read()

    print(data_1)

    # with open(file1, 'w') as a:
    #     a.write(data_1)

    # with open(file2, 'w') as b:
    #     b.write(data_2)

    f = open(file1, "w")
    f.write(data_2)
    f.close()

    g = open(file2, "w")
    g.write(data_1)
    g.close()

swapFileData()