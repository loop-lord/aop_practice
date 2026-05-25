def gradingStudents(grades: list[int]) -> list[int]:
    """Round each grade per HackerLand University's policy.

    Rules:
    - If ``grade`` is less than 38, it is not rounded (still failing).
    - Otherwise, if the next multiple of 5 is within 3 of ``grade``,
      round up to that multiple of 5; else leave it unchanged.
    """
    rounded: list[int] = []
    for grade in grades:
        if grade < 38:
            rounded.append(grade)
            continue

        if grade % 5 == 0:
            rounded.append(grade)
            continue

        next_multiple = grade + (5 - grade % 5)
        if next_multiple - grade < 3:
            rounded.append(next_multiple)
            continue

        rounded.append(grade)

    return rounded


if __name__ == "__main__":
    n = int(input().strip())
    grades_input = [int(input().strip()) for _ in range(n)]
    for result in gradingStudents(grades_input):
        print(result)
