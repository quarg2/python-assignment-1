# Print prices of items from a given shopping bill

def main():
    discount = 0
    freeItems = 0
    totalItems = 0
    totalPrice = 0
    i = 0;
    with open("purchases.txt", "r") as f:
        for line in f:
            if (len(line) > 1):
                item, price = line.split(" ")
                item, price = item.strip(), price.strip()
                if item == "Discount":
                    discount += int(price)
                else:
                    if price == "Free":
                        freeItems += 1
                    else:
                        totalItems += 1
                        totalPrice = totalPrice + int(price)




    print(f"Total items purchased: {totalItems}")
    print(f"Number of free items: {freeItems}")
    print(f"Amount (before discount): {totalPrice}")
    print(f"Discount given: {discount}")
    print(f"Amount to be paid: {totalPrice - discount}")


if __name__ == "__main__":
    main()