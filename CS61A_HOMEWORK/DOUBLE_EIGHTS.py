def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    sum,tmp=0,n
    while tmp>0:
        tmp,tmp1=tmp//10,tmp%10
        if tmp1==8:
            if tmp%10==8:
                sum+=1
    if sum>0:
        return True
    else:
        return False
