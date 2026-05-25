def staircase(n: int) -> None:
    for i in range(1, n + 1):
        print(("#" * i).rjust(n))


if __name__ == "__main__":
    n = int(input().strip())

    staircase(n)
