__author__ = 'Fang'

import re
import os
import copy


lines = []
SCHEMA = 300


def GetALineSchema(line, length, lineid, FAULT):
    diff = []
    idx = []
    newLine = copy.deepcopy(line)
    for i in range(length):
        diff.append(0)
        idx.append(i)
    for i in range(lineid, len(lines)):
        a = lines[i]
        if length == len(a):
            for j in range(length):
                if a[j] != newLine[j]:
                    diff[j] += 1
    idx.sort(key=lambda x: diff[x])
    fault = length - 1
    for i in range(length / 2, length - 1):
        if diff[idx[i + 1]] - diff[idx[i]] >= FAULT:
            fault = i
            break
    for i in range(fault + 1, length):
        newLine[idx[i]] = '*'
    return newLine


def GetAllSchema():
    l = 10
    r = 100
    best = []
    fzc  = []
    while l <= r:
        fault = (l + r) / 2
        print fault
        allSchema = []
        tmpfzc = []
        numSchema = 0
        for k in range(len(lines)):
            a = lines[k]
            length = len(a)
            for b in allSchema:
                if length == len(b):
                    for i in range(0, len(b)):
                        if b[i] != "*" and a[i] != b[i]:
                            break
                    else:
                        break
            else:
                allSchema.append(GetALineSchema(a, length, k, fault))
                tmpfzc.append(a)
                numSchema += 1
                if numSchema > SCHEMA:
                    r = fault - 1
                    break
        else:
            l = fault + 1
            fzc = tmpfzc
            best = allSchema
        print numSchema
    return best, fzc


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
    schema,fzc = GetAllSchema()
    for i in range(len(schema)):
        print schema[i]
        print fzc[i]

