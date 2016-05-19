__author__ = 'Fang'

import random

'''
kmeans++ algorithm
use SetData() to set the NUMBER of CLUSTERs, the LENGTH of VECTORs and the WORD VECTOR SET
use KmeansCluster() to get the CLUSTERs that each vector belongs to and the MEANS of clusters
'''


class KMeans:
    # cluster number
    k = 0
    # word vector's length
    n = 0
    # word vector set AND size
    w_vector = []
    m = 0
    # means
    means = []
    # list of cluster
    pre = []
    head = []
    # cluster that vector belongs to
    belong = []
    # number of vector changing cluster at least
    sentinel = 100
    # vector is sparse
    sparse = False

    def __init__(self, sp=False):
        self.sparse = sp

    def SetData(self, k=0, n=0, vector=[]):
        self.k = k
        self.n = n
        self.w_vector = vector
        self.m = len(self.w_vector)
        self.belong = [-1 for j in xrange(self.m)]
        self.sentinel = self.m / 1000

    # calculate the distance between vector a and vector b
    # spa = True means a is sparse and spb = True means b is sparse
    def CalDis(self, a, spa, b, spb):
        res = 0
        if not spa and not spb:
            for i in xrange(self.n):
                tmp = a[i] - b[i]
                res += tmp * tmp
        else:
            now = [0 for j in xrange(self.n)]
            if spa:
                for i in a:
                    now[i] += 1
            else:
                for i in xrange(self.n):
                    now[i] += a[i]
            if spb:
                for i in b:
                    now[i] -= 1
            else:
                for i in xrange(self.n):
                    now[i] -= b[i]
            for i in now:
                res += i * i
        return res

    # find the nearest mean
    def FindNearestMean(self, a, tmpmeans):
        best = 0
        dis = self.CalDis(a, self.sparse, tmpmeans[0], self.sparse)
        for i in xrange(1, len(tmpmeans)):
            tmpdis = self.CalDis(a, self.sparse, tmpmeans[i], self.sparse)
            if tmpdis < dis:
                dis = tmpdis
                best = i
        return tmpmeans[best]

    # get means for beginning
    def GetMeans(self):
        res = [random.choice(self.w_vector)]
        d = [-1 for i in xrange(self.m)]
        for i in xrange(1, self.k):
            sumd = 0
            for j in xrange(self.m):
                if d[j] == 0:
                    continue
                d[j] = self.CalDis(self.w_vector[j], self.sparse,
                                   self.FindNearestMean(self.w_vector[j], res), self.sparse)
                sumd += d[j]
            sumd *= random.random()
            for j in xrange(self.m):
                sumd -= d[j]
                if sumd <= 0:
                    res.append(self.w_vector[j])
                    break
        return res

    # match means and vectors
    def MatchMeans(self):
        head = [-1 for i in xrange(self.k)]
        pre = []
        belong = []
        changed = 0
        for i in xrange(self.m):
            best = 0
            dis = self.CalDis(self.w_vector[i], self.sparse, self.means[0], False)
            for j in xrange(1, self.k):
                tmpdis = self.CalDis(self.w_vector[i], self.sparse, self.means[j], False)
                if tmpdis < dis:
                    dis = tmpdis
                    best = j
            pre.append(head[best])
            head[best] = i
            belong.append(best)
            if best != self.belong[i]:
                changed += 1
        return pre, head, belong, changed

    # main method
    def KmeansCluster(self):
        self.means = self.GetMeans()
        # print "found k init means"
        numIter = 0
        while True:
            numIter += 1
            self.pre, self.head, self.belong, changed = self.MatchMeans()
            print "Iter is %d , change is %d ." % (numIter, changed)
            # find new means
            for i in xrange(self.k):
                newCenter = [0.0 for j in xrange(self.n)]
                idx = self.head[i]
                cnt = 0
                while idx != -1:
                    cnt += 1
                    for j in xrange(self.n):
                        newCenter[j] += self.w_vector[idx][j]
                    idx = self.pre[idx]
                if cnt > 0:
                    for j in xrange(self.n):
                        newCenter[j] /= cnt
                self.means[i] = newCenter
            if changed < self.sentinel or numIter > 10:
                break
        return self.belong, self.means
