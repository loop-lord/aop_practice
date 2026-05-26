from collections import Counter


def migratory_birds(arr: list[int]) -> int:
    """Return the id of the most frequently sighted bird type.

    Counts how often each bird type id appears in ``arr`` and returns the id
    with the highest frequency. If several ids share the maximum frequency,
    the smallest such id is returned.

    Args:
        arr: Bird type ids observed during the sightings. Must contain at
            least one element.

    Returns:
        The smallest id among the bird types tied for the highest sighting
        count.
    """
    counts = Counter(arr)
    return min(counts.items(), key=lambda item: (-item[1], item[0]))[0]


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    assert len(arr) == n

    print(migratory_birds(arr))
