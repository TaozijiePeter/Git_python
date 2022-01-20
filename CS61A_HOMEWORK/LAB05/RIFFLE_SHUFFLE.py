def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], ... where M is position of the
    second half of the deck.  Assume that len(DECK) is even.
    >>> riffle([3, 4, 5, 6])
    [3, 5, 4, 6]
    >>> riffle(range(20))
    [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
    """
    tmp1,tmp2,tmp3,k=deck[0:len(deck)//2:1],deck[len(deck)//2::1],[],0
    while k<min(len(tmp1),len(tmp2)):
        tmp3.append(tmp1[k])
        tmp3.append(tmp2[k])
        k+=1
    while k<len(tmp1):
        tmp3.append(tmp1[k])
        k+=1
    while k<len(tmp2):
        tmp3.append(tmp2[k])
        k+=1
    return tmp3

