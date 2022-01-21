def merge(incr_a, incr_b):
    """Yield the elements of strictly increasing iterables incr_a and incr_b, removing
    repeats. Assume that incr_a and incr_b have no repeats. incr_a or incr_b may be infinite
    sequences.

    >>> m = merge([0, 2, 4, 6, 8, 10, 12, 14], [0, 3, 6, 9, 12, 15])
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    >>> def big(n):
    ...    k = 0
    ...    while True: yield k; k += n
    >>> m = merge(big(2), big(3))
    >>> [next(m) for _ in range(11)]
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    iter_a, iter_b = iter(incr_a), iter(incr_b)
    next_a, next_b = next(iter_a, None), next(iter_b, None)
    while next_a is not None or next_b is not None:
        if next_a is None:
            yield next_b
            next_b = next(iter_b, None)
        elif next_b is None:
            yield next_a
            next_a = next(iter_a, None)
        else:
            if next_a < next_b:
                yield next_a
                next_a = next(iter_a, None)
            elif next_b < next_a:
                yield next_b
                next_b = next(iter_b, None)
            else:
                yield next_a
                next_a, next_b = next(iter_a, None), next(iter_b, None)


