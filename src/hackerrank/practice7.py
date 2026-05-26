def breaking_records(scores: list[int]) -> list[int]:
    """Return the number of times the best and worst scoring records are broken.

    The first game in ``scores`` establishes the initial highest and lowest
    records for the season; counting starts from the second game onward. A
    record is broken only when a later score is *strictly* greater than the
    current maximum (best record) or *strictly* less than the current minimum
    (worst record). Ties do not count.

    Args:
        scores: Points scored in each game, in chronological order. Must
            contain at least one game.

    Returns:
        A two-element list ``[max_breaks, min_breaks]`` where ``max_breaks``
        is the number of times the highest-score record was broken and
        ``min_breaks`` is the number of times the lowest-score record was
        broken across the season.
    """
    highest = lowest = scores[0]
    max_breaks = min_breaks = 0

    for score in scores[1:]:
        if score > highest:
            highest = score
            max_breaks += 1
        elif score < lowest:
            lowest = score
            min_breaks += 1

    return [max_breaks, min_breaks]


if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))

    assert len(scores) == n

    result = breaking_records(scores)
    print(" ".join(map(str, result)))
