from typing import List


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y
        count = 0
        while a != 0:
            a = a & (a - 1)
            count += 1
        return count

    def totalHammingDistance(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                a = nums[i] ^ nums[j]
                count = 0
                while a != 0:
                    a = a & (a - 1)
                    count += 1
                sum += count
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1, 4))
    print(s.totalHammingDistance([4, 14, 2]))
