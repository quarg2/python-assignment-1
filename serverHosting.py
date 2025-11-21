# Mobile hosting costs a certain amount per hour. Find cost per day, week, month
#  and how many days it can be operated for for a given amount


def main():
    COST_PER_HOUR = 0.51

    costPerDay = COST_PER_HOUR * 24
    costPerWeek = costPerDay * 7
    costPerMonth = costPerDay * 30

    print(f"Cost per day: {costPerDay}")
    print(f"Cost per week: {costPerWeek}")
    print(f"Cost per month: {costPerMonth}")

    GIVEN_AMOUNT = 918
    daysForGivenAmount = (GIVEN_AMOUNT / COST_PER_HOUR) / 24

    print(
        f"For a given amount {GIVEN_AMOUNT}, the server will \
          run for {daysForGivenAmount} days"
    )


if __name__ == "__main__":
    main()
