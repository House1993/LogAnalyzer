__author__ = 'Fang'

import re
import os


def GetContent(logName):
    log = []
    with open(logName) as inputfile:
        for line in inputfile:
            splits = line.strip().split(" ")
            if re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", splits[0]):
                log.append(splits[2:])
    return log


def WordFilter(log):
    dic = {}
    for line in log:
        for word in line:
            if not re.match("^[^a-zA-Z]*$", word):
                if word not in dic:
                    dic[word] = 0
                else:
                    dic[word] += 1
    lis = []
    length = 0
    for (k, v) in dic.items():
        lis.append((k, v))
        length += 1
    lis.sort(key=lambda x: (x[1], x[0]), reverse=True)
    return lis


if __name__ == "__main__":
    print "start reading raw"
    lines = []
    for i in os.listdir("raw"):
        lines.extend(GetContent("raw/" + i))
    print "finish reading"
    print "start selecting words"
    wordList = WordFilter(lines)
    print "finish selecting words"
    for i in wordList:
        print "%s\t\t%d" % (i[0], i[1])
