def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    tmp1,tmp2=[],range(lower,upper+1)
    for i in seq:
        if i**2 in tmp2:
            tmp1.append([i,i**2])
    return tmp1
