__author__ = 'Fang'

import re
import os
from kmeans import KMeans


def GetLog(logName, wordSet, wordNum):
    log = []
    with open(logName) as inputfile:
        for line in inputfile:
            splits = line.strip().split(" ")
            if re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", splits[0]):
                alog = [0 for i in xrange(wordNum)]
                for word in splits[2:]:
                    if word in wordSet.keys():
                        alog[wordSet[word]] += 1
                log.append(alog)
    return log


def GetWords(dicName):
    dic = {}
    num = 0
    with open(dicName) as infile:
        for line in infile:
            dic[line.split("\t", 1)[0]] = num
            num += 1
    return dic, num


def output(wds, wdn, vec, clu, mean):
    # SSE(Sum of squared errors)
    sse = 0
    kms = KMeans(False)
    for j in xrange(len(vec)):
        v = vec[j]
        m = mean[clu[j]]
        sse += kms.CalDis(v, kms.sparse, m, False)
    print "SSE is", sse
    # keywords of means
    words = [j for j in xrange(wdn)]
    for (k, v) in wds.items():
        words[v] = k
    print "means' keyword:"
    for m in mean:
        print m
        for j in xrange(wdn):
            if m[j] > 0.5:
                print words[j],
        print ""
    # belong
    print "belong :"
    for j in clu:
        print j,
    print ""
    # print "word set:"
    # print wds
    # print "vectors:"
    # for j in vec:
    #     print j

if __name__ == "__main__":
    # print "start reading dictionary"
    wordSet, wordNum = GetWords("result5")
    # print "finish reading"
    # print "start reading raw"
    vectors = []
    lsfile = os.listdir("raw")
    lsfile.sort()
    for i in lsfile:
        print i
        vectors.extend(GetLog("raw/" + i, wordSet, wordNum))
    # print "finish reading"
    # print "kmeans starts"
    kcluster = 50
    kmeansalgo = KMeans(False)
    kmeansalgo.SetData(kcluster, wordNum, vectors)
    belong, means = kmeansalgo.KmeansCluster()
    # print "kmeans ends"
    # output some arguments
    output(wordSet, wordNum, vectors, belong, means)
