def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row. Iterate through the items such that
    if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
    in the first.

    >>> lst = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(lst, 2)
    9
    >>> lst2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(lst2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    last = next(t)
    occur_times = 1
    for v in t:
        if v == last:
            occur_times += 1
            if occur_times == k:
                return v
        else:
            occur_times = 1
            last = v

