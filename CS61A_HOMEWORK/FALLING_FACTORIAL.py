def falling(n,k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    if k==0:
        return 1
    else:
        tmp,index=k-1,n
        while tmp>0:
            tmp,index=tmp-1,index*(n-tmp)
        return index

