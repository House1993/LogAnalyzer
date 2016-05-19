__author__ = 'Fang'

import re
import os
import copy


lines = []


def GetALineSchema(line, length, lineid):
    diff = []
    idx = []
    newLine = copy.deepcopy(line)
    for k in range(length):
        diff.append(0)
        idx.append(k)
    for k in range(lineid, len(lines)):
        a = lines[k]
        if length == len(a):
            for j in range(length):
                if a[j] != newLine[j]:
                    diff[j] += 1
    idx.sort(key=lambda x: diff[x])
    fault = length / 2
    for k in range(length / 2, length - 1):
        if diff[idx[k + 1]] - diff[idx[k]] > diff[idx[fault + 1]] - diff[idx[fault]]:
            fault = k
    for k in range(fault + 1, length):
        newLine[idx[k]] = '*'
    return newLine


def GetAllSchema():
    allSchema = []
    fzc = []
    for k in range(len(lines)):
        a = lines[k]
        length = len(a)
        for b in allSchema:
            if length == len(b):
                for j in range(0, len(b)):
                    if b[j] != "*" and a[j] != b[j]:
                        break
                else:
                    break
        else:
            allSchema.append(GetALineSchema(a, length, k))
            fzc.append(a)
    return allSchema, fzc


def GetContent(logName):
    log = []
    with open(logName) as inputfile:
        for line in inputfile:
            splits = line.strip().split(" ")
            if re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", splits[0]):
                log.append(splits[2:])
    return log


if __name__ == "__main__":
    for i in os.listdir("raw"):
        lines.extend(GetContent("raw/" + i))
    schema, fzc = GetAllSchema()
    for i in range(len(schema)):
        print schema[i]
        print fzc[i]
