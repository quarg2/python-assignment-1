# Given a student's name and marks in three subjects, calculate their
#  total and average marks


def main():
    name = input("Enter student name: ")
    marks1 = float(input("Enter student's marks in subject 1: "))
    marks2 = float(input("Enter student's marks in subject 2: "))
    marks3 = float(input("Enter student's marks in subject 3: "))

    try:
        grading = grade(marks1, marks2, marks3)
        print(f"The total marks is {grading[0]}")
        print(f"The average marks is {grading[1]}")
        print(f"The grade is {grading[2]}")
    except ValueError:
        print("Error: Grade not between 0 and 100 (both inclusive)")


def grade(*marks) -> tuple[float, float, str]:
    """
    Returns a tuple containing the total, average, and the grade of a given
    student's marks.
    Arguments:
        *marks: marks in various subjects
    Returns:
        (total, average, grade): Total marks, average marks, and the grade
            (according to CBSE)
    Raises:
        ValueError: If 0 <= grade <= 100 is not true
    """
    if False in map(lambda x: 0 <= x <= 100, marks):
        raise ValueError("Marks not between 0 and 100 (both inclusive)")
    else:
        total = sum(marks)
        average = total / len(marks)

    if 90 < total <= 100:
        grade = "A1"
    elif 80 < total <= 90:
        grade = "A2"
    elif 70 < total <= 80:
        grade = "B1"
    elif 60 < total <= 70:
        grade = "B2"
    elif 50 < total <= 60:
        grade = "C1"
    elif 40 < total <= 41:
        grade = "C2"
    elif 33 < total <= 40:
        grade = "D"
    elif 20 < total <= 33:
        grade = "E1"
    else:
        grade = "E2"

    return total, average, grade


if __name__ == "__main__":
    main()
