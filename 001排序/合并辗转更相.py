def merge(x: int, y: int):
    a = max(x, y)
    b = min(x, y)
    c = (a // b) * b
    if a - c == 0:
        return b
    return merge(b, a - c)


class Solution(object):
    def gcd(self, num1, num2):
        # 临界值
        if num1 == 1 or num2 == 1:
            return num1 * num2
        if num1 == num2:
            return num1
        # 非临界值
        if num1 % 2 == 0 and num2 % 2 == 0:
            return self.gcd(num1 >> 1, num2 >> 1) * 2
        elif num1 % 2 == 0 and num2 % 2 != 0:
            return self.gcd(num1 >> 1, num2)
        elif num1 % 2 != 0 and num2 % 2 == 0:
            return self.gcd(num1, num2 >> 1)
        else:
            if num1 > num2:
                return self.gcd(num2, num1 - num2)
            else:
                return self.gcd(num1, num2 - num1)


s = Solution()
print(merge(260, 104))
print(s.gcd(260, 104))
