from LINK_LIST import *
def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    if s==Link.empty or s.rest==Link.empty:
        return 
    k,tmp=1,s.first
    s=s.rest
    while s.rest!=Link.empty:
        if k%2==0:
            tmp=tmp+s.first
        s,k=s.rest,k+1
    if k%2==0:
        tmp=tmp+s.first
    s=tmp

