def centerSpread(strs, left, right) -> str:
    length = len(strs)
    i = left
    j = right
    while i >= 0 and j < length:
        if strs[i] == strs[j]:
            i -= 1
            j += 1
        else:
            break
    return strs[i + 1:j]


def longestPalindrome(s: str) -> str:
    length = len(s)
    if len(s) < 2:
        return s
    maxlen = 1
    res = s[0]
    for i in range(length):
        odd = centerSpread(s, i, i)
        even = centerSpread(s, i, i + 1)
        maxstr = odd if len(odd) > len(even) else even
        if len(maxstr) > maxlen:
            maxlen = len(maxstr)
            res = maxstr
    return res


if __name__ == '__main__':
    strs = "01000120203400"
    print(longestPalindrome(strs))