# Mode of transport for given distance

def main():
    distance = float(input("Enter distance: "))

    if distance < 3:
        print("A bicycle can be used")
    elif 3 <= distance < 300:
        print("A motorcycle can be used")
    else:
        print("A car can be used")

if __name__ == "__main__":
    main()