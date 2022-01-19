def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def helper(n,m):
        if n==0:
            return 1
        elif n<(1<<m):
            return 0
        else:
            return helper(n,m+1)+helper(n-(1<<m),m)
    return helper(total,0)
