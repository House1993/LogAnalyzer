__author__ = 'Fang'

import matplotlib.pyplot as plt

if __name__ == "__main__":
    plt.xlabel('Interval')
    plt.ylabel('Count')
    plt.title('Time Interval')
    lis = []
    cnt = 0.0
    with open("Result7", "r") as infile:
        for line in infile:
            sp = line.strip().split(" ", 1)
            x = int(sp[0])
            y = int(sp[1])
            lis.append((x, y))
            cnt += y
    ff = 0.0
    for i in xrange(40):
        if lis[i][0] > 30:
            break
        ff += lis[i][1] / cnt
    print ff
    for i in xrange(1, len(lis)):
        if lis[i][0] > 30:
            break
        plt.plot([lis[i - 1][0], lis[i][0]], [lis[i - 1][1] / cnt, lis[i][1] / cnt], 'r')
    plt.show()
