def pascal(row, column):
    """Returns a number corresponding to the value at that location
    in Pascal's Triangle.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 4 (1 3 3 1), 3rd entry
    3
    """
    if column>row:
        return 0
    elif column==row:
        return 1
    elif column==0:
        return 1
    else:
        return pascal(row-1,column)+pascal(row-1,column-1)
