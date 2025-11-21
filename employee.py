# Get employee name and salary from user. Then print their name and total salary

def main():
    employees = dict({})
    while True:
        name = input("Enter name of employee (enter `stop' to stop): ")

        if name == "stop":
            break

        salary = float(input("Enter salary: "))

        hra = salary * 0.2
        da = salary * 0.1

        employees[name] = (salary, hra, da)

    print("Employee salaries")
    for k, v in employees.items():
        print(f"{k}: {sum(v)}")

if __name__ == "__main__":
    main()