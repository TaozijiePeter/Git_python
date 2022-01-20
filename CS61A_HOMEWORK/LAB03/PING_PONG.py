from NUM_EIGHTS import num_eights
def pingpong(n):
    """Return the nth element of the ping-pong sequence.
    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(i, state, direction):
        if i == n:
            return state
        if num_eights(i) != 0 or i % 8 == 0:
            return helper(i + 1, state - direction, direction*-1)
        else:
            return helper(i + 1, state + direction, direction)

    return helper(1, 1, 1)

