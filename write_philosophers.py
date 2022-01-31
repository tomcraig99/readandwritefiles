def main():
    # open the file

    outfile = open("philosophers.txt", "w")

    # create variables for names

    name1 = "John Locke"
    name2 = "David Hume"
    name3 = "Edmund Burke"

    # write the names into the file

    outfile.write(name1 + "\n")
    outfile.write(name2 + "\n")
    outfile.write(name3 + "\n")

    # close the file

    outfile.close()


def add_my_name():
    outfile = open("philosophers.txt", "a")

    name = "Thomas Craig"

    outfile.write(name)

    outfile.close()


# invoke main
main()
add_my_name()
