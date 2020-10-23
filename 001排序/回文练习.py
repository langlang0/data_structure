def centerSpread(strs: str, left, right) -> str:
    i = left
    j = right
    length = len(strs)
    while i >= 0 and j < length:
        if strs[i] == strs[j]:
            i -= 1
            j += 1
        else:
            break
    return strs[i + 1:j]


def longestPalindrome(strs: str) -> str:
    length = len(strs)
    if length < 2:
        return strs
    maxlen = 1
    res = strs[0]
    for i in range(length - 1):
        odd = centerSpread(strs, i, i)
        even = centerSpread(strs, i, i + 1)
        maxstr = odd if len(odd) > len(even) else even
        if len(maxstr) > maxlen:
            maxlen = len(maxstr)
            res = maxstr
    return res


def centerSpreads(strs, left, right) -> str:
    i = left
    j = right
    length = len(strs)
    while i >= 0 and j < length:
        if strs[i] == strs[j]:
            i -= 1
            j += 1
        else:
            break
    return strs[i + 1:j]

def maxLengthstr(strs:str):
    length = len(strs)
    if length < 2:
        return strs
    maxlen = 1
    res = strs[0]
    for i in range(length - 1):
        odd = centerSpreads(strs,i,i)
        even = centerSpreads(strs,i,i + 1)
        maxstr = odd if len(odd) > len(even) else even
        if len(maxstr) > maxlen:
            maxlen = len(maxstr)
            res = maxstr
    return res













