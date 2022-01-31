def main():
    infile = open("clients.txt", "r")

    i = 1
    for name in infile:
        name = name.rstrip("\n")
        print(str(i) + ".", name)
        i += 1
    infile.close()


main()
