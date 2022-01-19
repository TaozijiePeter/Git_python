def both_paths(sofar="S"):
    """
    >>> up, down = both_paths()
    S
    >>> upup, updown = up()
    SU
    >>> downup, downdown = down()
    SD
    >>> _ = upup()
    SUU
    """
    print(sofar)
    def up():
        sofar1=sofar+"U"
        return both_paths(sofar1)
    def down():
        sofar2=sofar+"D"
        return both_paths(sofar2)
    return up,down
