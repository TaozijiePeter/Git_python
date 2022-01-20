def reverse_iter(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    tmp=[]
    for i in range(len(lst)):
        tmp.append(lst[len(lst)-1-i])
    return tmp

def reverse_recursive(lst):
    """Returns the reverse of the given list.

    >>> reverse_recursive([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    if len(lst)<=1:
        return lst
    else:
        return [lst[len(lst)-1]]+reverse_recursive(lst[1:len(lst)-1])+[lst[0]]
