def solution(participant, completion):
    hash_sum = 0
    part = {}
    for i in participant:
        hash_sum += hash(i)
        part[hash(i)] = i
    for i in completion:
        hash_sum -= hash(i)
    return part[hash_sum]