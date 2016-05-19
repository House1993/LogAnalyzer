__author__ = 'Fang'

import os
import re
import time
import math

if __name__ == "__main__":
    cnt = dict()
    last_ms = -1
    file_list = os.listdir("raw")
    file_list.sort()
    for i in xrange(len(file_list) - 1, -1, -1):
        with open("raw/" + file_list[i]) as infile:
            for line in infile:
                sp = line.strip().split(" ", 2)
                if re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", sp[0]):
                    spp = sp[1].split(",", 1)
                    now_s = time.strptime(sp[0] + " " + spp[0], "%Y-%m-%d %H:%M:%S")
                    now_ms = time.mktime(now_s) + int(spp[1]) / 1000.0
                    if last_ms > 0:
                        sub = now_ms - last_ms
                        tmp = int(math.ceil(sub))
                        if 0 > sub > -1:
                            print file_list[i]
                            print line
                        if tmp in cnt.keys():
                            cnt[tmp] += 1
                        else:
                            cnt[tmp] = 1
                    last_ms = now_ms
    lis = list()
    for (k, v) in cnt.items():
        lis.append((k, v))
    lis.sort(key=lambda x: (x[0], x[1]))
    for i in lis:
        print i[0], i[1]
