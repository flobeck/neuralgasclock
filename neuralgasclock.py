import codebookvector as cbv
import digit
import datetime
import numpy as np

W  = 900.0; H = 300.0;
N = 30 # number of codebook vectors per digit

def halton(index, base):
    res = 0.0; f = 1/base; i = index
    while (i > 0):
        res = res + f*(i%base)
        i = np.floor(i/base)
        f = f/base
    return res

def initCBV(i,j):
    return cbv.CodeBookVector((halton(i,2.0)+j)*(W/6.0),     #x
                              halton(i,3.0)*H,               #y
                              1.0,                           #t
                              8.0,                           #neighb.
                              1.0,                           #learn
                              i)                             #order

TimeGas = [[initCBV(i,j) for i in xrange(N)] for j in xrange(6)]


def metric(m, vec1, vec2):
    assert len(vec1) == len(vec2)
    if   m == "l1":   return np.linalg.norm((np.array(vec1)-np.array(vec2)), ord=1)
    elif m == "l2":   return np.linalg.norm((np.array(vec1)-np.array(vec2)), ord=2)
    else:             raise NameError('Metric %s not in scope. Try l1 or l2!' % m)


def qsort(cbv, vec):
    """
    sort codebook vectors with respect
    to some metric and a given vector vec
    """
    sortedCBV = []
    if len(cbv) == 0:
        return []
    else:
        p          = metric("l2", [cbv[0].x, cbv[0].y], vec) #value of pivotelement
        lesser     = qsort([tg for tg in cbv[1:] if metric("l2", [tg.x, tg.y], vec) <  p], vec)
        greater    = qsort([tg for tg in cbv[1:] if metric("l2", [tg.x, tg.y], vec) >= p], vec)
        sortedCBV  = lesser + [cbv[0]] + greater

    i = 1
    for e in sortedCBV:
        e.changeOrder(i)
        i = i+1
    return sortedCBV


def newDigit(now, upperleft):
    digitsDistribution = np.zeros((6,2))

    if now.minute%59 == 0 and now.hour%10 == 0:
        for i in range(N): TimeGas[0][i].resetTime()
    if now.minute%59 == 0 and now.hour%10 != 0:
        for i in range(N): TimeGas[1][i].resetTime()
    if now.minute%10 == 0 and now.second%60 == 0:
        for i in range(N): TimeGas[2][i].resetTime()
    if now.second%60 == 0:
        for i in range(N): TimeGas[3][i].resetTime()
    if now.second%10 == 0:
        for i in range(N): TimeGas[4][i].resetTime()
    if int(str(now.microsecond)[:4]) > 950:
        for i in range(N): TimeGas[5][i].resetTime()

    time = map(int, str(now.strftime('%H%M%S')))

    for i in xrange(6):
        shift = 120*i
        if   i == 2 or i == 3: shift = shift + 50
        elif i == 4 or i == 5: shift = shift + 100

        digitsDistribution[i] = digit.frequencyDistribution(20+shift,
                                                            50,
                                                            time[i],
                                                            100.0)
        if upperleft:
            digitsDistribution[i][1] = H - digitsDistribution[i][1]

    return digitsDistribution
