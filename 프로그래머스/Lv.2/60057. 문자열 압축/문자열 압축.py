def solution(s):
    min_value = len(s);
    for i in range(1, len(s) // 2 + 1):
        length = 0
        j = 0
        while j + i <= len(s): 
            h = j + i
            count = 1
            seg = s[j:j+i]
            while h + i <= len(s) and seg == s[h:h+i]:
                h += i
                count += 1 
            if count == 1:
                length += i;
            else:
                length += i + len(str(count));  
            j = h;
        if len(s) % i != 0:
            length += len(s) % i
        min_value = min(min_value, length)
    return min_value