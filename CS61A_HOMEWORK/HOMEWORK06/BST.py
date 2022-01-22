from TREES import *
def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    def bst_min(t):
        if t.is_leaf():
            return t.label
        elif len(t.branches) == 1:
            if t.label > t.branches[0].label:
                return bst_min(t.branches[0])
            else:
                return t.label
        else:
            return bst_min(t.branches[0])

    def bst_max(t):
        if t.is_leaf():
            return t.label
        elif len(t.branches) == 1:
            if t.label < t.branches[0].label:
                return bst_max(t.branches[0])
            else:
                return t.label
        else:
            return bst_max(t.branches[1])

    if t.is_leaf():
        return True
    if len(t.branches) == 1:
        if t.label > t.branches[0].label:
            return is_bst(t.branches[0]) and t.label >= bst_max(t.branches[0])
        else:
            return is_bst(t.branches[0]) and t.label < bst_min(t.branches[0])
    elif len(t.branches) == 2:
        le, ri = t.branches
        return is_bst(le) and is_bst(ri) and (bst_max(le) <= t.label < bst_min(ri))
    else:
        return False
