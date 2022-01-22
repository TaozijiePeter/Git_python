class Tree:
    def __init__(self,label,branches=[]):
        self.label=label
        for branch in branches:
            assert isinstance(branch,Tree)
        self.branches=list(branches)
    def __repr__(self):
        if self.branches:
            branches_repr=', '+repr(self.branches)
        else:
            branches_repr=''
        return 'Tree({0}{1})'.format(repr(self.label),branches_repr)
