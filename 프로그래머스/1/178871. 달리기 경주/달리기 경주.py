from collections import OrderedDict, deque
def solution(players, callings):
    dq_p = deque(players)
    dict_p = OrderedDict(map(lambda x:(x[1],x[0]), enumerate(players)))
    for s in callings:
        idx = dict_p[s]
        dq_p[idx-1], dq_p[idx] = s, dq_p[idx-1]
        dict_p[s] = dict_p[s]-1
        dict_p[dq_p[idx]] = dict_p[s] + 1
    sorted_p = sorted(dict_p.items(), key=lambda x: x[1])
    result = dict(sorted_p)
    return list(result.keys())