def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    """
    def helper(n):
        tmp1,tmp2=n//10,n%10
        if n==0:
            return 0
        elif tmp2==8:
            return helper(tmp1)+1
        else:
            return helper(tmp1)
    return helper(x)
