# Output a dictionary whose keys are odd numbers in a given list and values are
#  the key's square

def main():
    inp = []

    while True:
        n = input("Enter a number [non-numeric characters to stop]: ")

        if n.isnumeric():
            inp.append(int(n))
        else:
            break

    squares = {n: n ** 2 for n in inp if n % 2 != 0}

    print(squares)

if __name__ == main():
    main()