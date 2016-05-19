__author__ = 'Fang'


def prepare_db():
    lenseq = 1000
    res = []
    with open("Result3_part_belong.txt", "r") as infile:
        for line in infile:
            splites = line.split(" ")
            for i in xrange(len(splites)):
                splites[i] = [splites[i]]
            for i in xrange(lenseq, len(splites)):
                res.append(splites[i - lenseq: i])
    return res


if __name__ == "__main__":
    print "prepare database"
    db = prepare_db()
    print "db:"
    for dbi in db:
        print dbi
        # print "prefixspan start"
        # ps = prefixspan.PrefixSpan()
        # ps.set_data(db, 10000)
        # patterns = ps.prefix_span()
        # print "prefixspan end"
        # print "patterns:"
        # for ptn in patterns:
        #     print ptn
