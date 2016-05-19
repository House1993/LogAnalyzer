import re

res = list()
dic = set()
with open("stopwords.txt", "r") as infile:
    for line in infile:
        dic.add(line.strip())
with open("Result4", "r") as infile:
    for line in infile:
        tmp = line.split("\t")
        if int(tmp[-1]) < 10:
            break
        if not re.search("\d+ms", tmp[0]) and \
                not re.search("\d+\.\d+\.\d+\.\d+", tmp[0]) and \
                not re.search("DFSClient_hb_rs_hadoop", tmp[0]) and \
                not re.search("DFSClient_NONMAPREDUCE_", tmp[0]) and \
                not re.search("DFSClient_attempt_", tmp[0]) and \
                not re.search("(\w+\.)+\w+", tmp[0]) and \
                not re.search("(/\w+)+", tmp[0]) and \
                not re.search("([0-9a-zA-Z]+-){4}", tmp[0]) and \
                not re.search("=\d+", tmp[0]):
            ss = ""
            for i in line:
                if "z" >= i >= "a" or "Z" >= i >= "A" or i == "_" or i == "'":
                    ss += i
            if ss.lower() not in dic:
                # print ss
                res.append(tmp[0] + "\t\t" + tmp[-1])
with open("Result5", "w") as outfile:
    for line in res:
        outfile.write(line)
