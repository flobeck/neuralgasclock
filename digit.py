import numpy as np

"""
7-segment display:

    1
   ___
2 |   | 4
  |_3_|
  |   |
5 |___| 7
    6
  ^
  |
  reference point (x,y)

"""

def r(a,b): return np.random.uniform(a,b)

def frequencyDistribution(x, y, digit, scale):
    c1 = [r(x, x+scale), y+2*scale]
    c2 = [x,r(y+scale,y+2*scale)]
    c3 = [r(x,x+scale),y+scale]
    c4 = [x+scale,r(y+scale,y+2*scale)]
    c5 = [x,r(y,y+scale)]
    c6 = [r(x,x+scale),y]
    c7 = [x+scale,r(y,y+scale)]

    if digit == 0:
        zero = [c1,c2,c4,c5,c6,c7]
        return zero[int(r(0, 6))]

    elif digit == 1:
        one = [c4,c7]
        return one[int(r(0, 2))]

    elif digit == 2:
        two = [c1,c4,c3,c5,c6]
        return two[int(r(0, 5))]

    elif digit == 3:
        three = [c1,c3,c4,c6,c7]
        return three[int(r(0, 5))]

    elif digit == 4:
        four = [c2,c3,c4,c7]
        return four[int(r(0, 4))]

    elif digit == 5:
        five = [c1,c2,c3,c6,c7]
        return five[int(r(0, 5))];

    elif digit == 6:
        six = [c1,c2,c3,c5,c6,c7]
        return six[int(r(0, 6))];

    elif digit == 7:
        seven = [c1,c4,c7]
        return seven[int(r(0, 3))];

    elif digit == 8:
        eight = [c1,c2,c3,c4,c5,c6,c7]
        return eight[int(r(0, 7))]

    elif digit == 9:
        nine = [c1,c2,c3,c4,c6,c7]
        return nine[int(r(0, 6))]


    return [0,0]
