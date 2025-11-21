# Given 12 speed values, calculate the average speed and display the speed of
#  traffic flow

def main():
    speed = []

    for i in range(0, 12):
        speed.append(float(input(f"Enter speed for hour {i + 1}: ")))

    averageSpeed = sum(speed) / 12
    print(f"Average speed: {averageSpeed}")

    if averageSpeed < 40:
        print("Slow")
    elif averageSpeed < 80:
        print("Normal")
    else:
        print("Fast")


if __name__ == "__main__":
    main()