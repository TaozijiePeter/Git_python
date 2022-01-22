class Link:
    """A linked list.

    >>> s = Link(3, Link(4, Link(5)))
    >>> s
    Link(3, Link(4, Link(5)))
    >>> print(s)
    <3 4 5>
    >>> s.first
    3
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.first
    4
    >>> s.rest.first = 7
    >>> s
    Link(3, Link(7, Link(5)))
    >>> s.first = 6
    >>> s.rest.rest = Link.empty
    >>> s
    Link(6, Link(7))
    >>> print(s.rest)
    <7>
    >>> t = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> t
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(t)
    <1 <2 3> 4>

    >>> s.second
    7
    >>> s.second = 8
    >>> print(s)
    <6 8>
    >>> s1=6
    >>> s2=Link(3, Link(7, Link(5)))
    >>> s3=s2+s1
    >>> s3
    Link(3, Link(7, Link(5, Link(6))))
    """
    empty=()
    def __init__(self,first,rest=empty):
        assert rest is Link.empty or type(rest)==Link
        self.first=first
        self.rest=rest
    def __repr__(self):
        if self.rest:
            rest_repr=', '+repr(self.rest)
        else:
            rest_repr=''
        return 'Link('+repr(self.first)+rest_repr+')'
    def __str__(self):
        string='<'
        while self.rest is not Link.empty:
            string +=str(self.first)+' '
            self=self.rest
        return string+str(self.first)+'>'
    def __add__(self,other):
        if self.rest==Link.empty:
            self.rest=Link(other)
            return self
        else:
            return Link(self.first,self.rest+other)
    @property
    def second(self):
        return self.rest.first
    @second.setter
    def second(self,value):
        self.rest.first=value
