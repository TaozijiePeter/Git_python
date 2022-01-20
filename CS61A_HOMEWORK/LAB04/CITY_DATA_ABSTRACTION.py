def make_city(name,lat,lon):
    """>>> berkeley = make_city('Berkeley', 122, 37)
    >>> get_name(berkeley)
    'Berkeley'
    >>> get_lat(berkeley)
    122
    >>> new_york = make_city('New York City', 74, 40)
    >>> get_lon(new_york)
    40"""

    def helper1(tmp):
        if tmp==1:
            return name
        elif tmp==2: 
            return lat
        else:
            return lon
    return helper1
def get_name(city):
    """>>> berkeley = make_city('Berkeley', 122, 37)
    >>> get_name(berkeley)
    'Berkeley'
    """
    return city(1)
def get_lat(city):
    """>>> berkeley = make_city('Berkeley', 122, 37) 
    >>> get_lat(berkeley)
    122
    """
    return city(2)
def get_lon(city):
    """>>> new_york = make_city('New York City', 74, 40)
     >>> get_lon(new_york)
     40"""
    return city(3)

from math import sqrt
def distance(city_a, city_b):
    """
    >>> city_a = make_city('city_a', 0, 1)
    >>> city_b = make_city('city_b', 0, 2)
    >>> distance(city_a, city_b)
    1.0
    >>> city_c = make_city('city_c', 6.5, 12)
    >>> city_d = make_city('city_d', 2.5, 15)
    >>> distance(city_c, city_d)
    5.0
    """
    "*** YOUR CODE HERE ***"
    dis1=get_lat(city_a)-get_lat(city_b)
    dis2=get_lon(city_a)-get_lon(city_b)
    dis=(dis1**2+dis2**2)**(1/2)
    return dis
def closer_city(lat,lon,city_a,city_b):
    """
    Returns the name of either city_a or city_b, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    my_city=make_city('DUKE',lat,lon)
    tmp1,tmp2=distance(my_city,city_a),distance(my_city,city_b)
    return get_name(city_a) if tmp1<=tmp2 else get_name(city_b)
