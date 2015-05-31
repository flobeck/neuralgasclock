from neuralgasclock import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate(i):
    plt.clf()
    time = datetime.datetime.now()
    d = newDigit(time, False)
    x = np.array([]); y = np.array([])

    for i in xrange(6):  qsort(TimeGas[i], d[i])

    for digit in xrange(6):
        for particle in xrange(N):
            TimeGas[digit][particle].learn(d[digit][0],d[digit][1])
            x = np.append(x, TimeGas[digit][particle].x)
            y = np.append(y, TimeGas[digit][particle].y)

    plt.axis([0,W,0,H])
    plt.scatter(x,y,marker='o',s=1.0)


fig = plt.figure(figsize=(10, 4),dpi=80)
ani = animation.FuncAnimation(fig, animate, interval=10, blit=False)
plt.show()
