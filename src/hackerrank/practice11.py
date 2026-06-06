def pageCount(n: int, p: int) -> int:
    """Return the minimum number of pages to turn to reach a given page.

    A book has ``n`` pages. Page 1 sits alone on the right side, then each
    subsequent sheet holds two pages (an even page on the left and an odd page
    on the right). A reader may start turning pages from the front or from the
    back of the book, whichever is closer to the target page.

    Page ``k`` always lies on sheet ``k // 2``, so the number of turns from the
    front is ``p // 2`` and the number of turns from the back is
    ``n // 2 - p // 2``. Using ``n // 2`` for the final sheet correctly handles
    the case where the last page is printed on only the front side.

    Args:
        n: The number of pages in the book.
        p: The page number to turn to.

    Returns:
        The minimum number of pages that must be turned to arrive at page ``p``.
    """
    from_front = p // 2
    from_back = n // 2 - p // 2
    return min(from_front, from_back)


if __name__ == "__main__":
    n = int(input().strip())

    p = int(input().strip())

    print(pageCount(n, p))
