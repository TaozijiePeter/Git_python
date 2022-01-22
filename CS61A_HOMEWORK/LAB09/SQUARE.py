from TREES import *
def label_squarer(t):
    """Mutates a Tree t by squaring all its elements.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> label_squarer(t)
    >>> t
    Tree(1, [Tree(9, [Tree(25)]), Tree(49)])
    """
    t.label=t.label**2 
    if not t.branches:
        return 
    else:
        for branch in t.branches:
            label_squarer(branch)

