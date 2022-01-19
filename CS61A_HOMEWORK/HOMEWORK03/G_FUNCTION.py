def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n<=3:
        return n
    else:
        return g(n-1)+2*g(n-2)+3*g(n-3)
def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    g_1,g_2,g_3,k=1,2,3,3
    if n<=3:
        return n;
    else:
        while k<n:
            g_1,g_2,g_3,k=g_2,g_3,3*g_1+2*g_2+g_3,k+1
        return g_3
    
