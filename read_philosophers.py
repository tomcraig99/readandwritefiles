def main():
    # open the file
    infile = open("philosophers.txt", "r")
    # read the contents
    line1 = infile.readline().rstrip("\n")
    line2 = infile.readline().rstrip("\n")
    line3 = infile.readline().rstrip("\n")
    # print the contents
    print(line1)
    print(line2)
    print(line3)
    # close the file
    infile.close()


# invoke main
main()
