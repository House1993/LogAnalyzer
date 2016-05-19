__author__ = 'Fang'

'''
PrefixSpan algorithm
use set_data() to set the initial SEQUENCE DATABASE and the MINIMUM SUPPORT THRESHOLD
use prefix_span() to get all PATTERNs
'''


class PrefixSpan:
    # sequence
    sequence = []
    # min_support
    min_support = 0
    # answer
    ans = []

    def __init__(self):
        pass

    def set_data(self, seq=list(), min_sup=0):
        self.sequence = seq
        self.min_support = min_sup

    def dfs(self, db, prefix):
        tmp_db_now = dict()
        tmp_db_now_size = dict()
        tmp_db_next = dict()
        tmp_db_next_size = dict()
        for i in db:
            off_seq_idx = i[0]
            off_ele_idx = i[1]
            off_itm_idx = i[2]
            seq = self.sequence[off_seq_idx]
            vis = set()
            for itm_idx in range(off_itm_idx + 1, len(seq[off_ele_idx])):
                itm = seq[off_ele_idx][itm_idx]
                if itm not in vis:
                    vis.add(itm)
                    if itm in tmp_db_now_size.keys():
                        tmp_db_now[itm].append((off_seq_idx, off_ele_idx, itm_idx))
                        tmp_db_now_size[itm] += 1
                    else:
                        tmp_db_now[itm] = [(off_seq_idx, off_ele_idx, itm_idx)]
                        tmp_db_now_size = 1
            vis = set()
            for ele_idx in range(off_ele_idx + 1, len(seq)):
                ele = seq[ele_idx]
                itm_idx = 0
                for itm in ele:
                    if itm not in vis:
                        vis.add(itm)
                        if itm in tmp_db_next_size.keys():
                            tmp_db_next[itm].append((off_seq_idx, ele_idx, itm_idx))
                            tmp_db_next_size[itm] += 1
                        else:
                            tmp_db_next[itm] = [(off_seq_idx, ele_idx, itm_idx)]
                            tmp_db_next_size[itm] = 1
                    itm_idx += 1
        for (postfix, num) in tmp_db_now_size.items():
            if num >= self.min_support:
                prefix[-1].append(postfix)
                self.ans.append(prefix)
                self.dfs(tmp_db_now[postfix], prefix)
                prefix[-1].pop()
        for (postfix, num) in tmp_db_next_size.items():
            if num >= self.min_support:
                prefix.append([postfix])
                self.ans.append(prefix)
                self.dfs(tmp_db_next[postfix], prefix)
                prefix.pop()

    def prefix_span(self):
        self.ans = list()
        tmp_db = dict()
        tmp_db_size = dict()
        seq_idx = 0
        for seq in self.sequence:
            vis = set()
            ele_idx = 0
            for ele in seq:
                itm_idx = 0
                for itm in ele:
                    if itm not in vis:
                        vis.add(itm)
                        if itm in tmp_db_size.keys():
                            tmp_db[itm].append((seq_idx, ele_idx, itm_idx))
                            tmp_db_size[itm] += 1
                        else:
                            tmp_db[itm] = [(seq_idx, ele_idx, itm_idx)]
                            tmp_db_size[itm] = 1
                    itm_idx += 1
                ele_idx += 1
            seq_idx += 1
        for (prefix, num) in tmp_db_size.items():
            if num >= self.min_support:
                self.ans.append([[prefix]])
                self.dfs(tmp_db[prefix], [[prefix]])
        return self.ans
