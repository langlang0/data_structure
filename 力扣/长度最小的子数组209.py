from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        mins = len(nums)
        for i in range(len(nums)):
            sums = 0
            count = 0
            while sums <= s and i < len(nums):
                sums += nums[i]
                count += 1
                if sums < s:
                    i += 1
                    continue
                if sums > s:
                    mins = count
                    break
                if count < mins and sums == s:
                    mins = count
        return mins


# 正确思路   滑动窗口,类似尺蠖爬动
class Solution1:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        sums = 0
        res = len(nums) + 1
        for right in range(len(nums)):
            sums += nums[right]
            while sums >= s:
                if right - left + 1 < res:
                    res = right - left + 1
                sums -= nums[left]
                left += 1
        return 0 if res == len(nums) + 1 else res


if __name__ == '__main__':
    s = 11
    nums = [1, 2, 3, 4, 5]
    a = Solution()
    b = a.minSubArrayLen(s, nums)
    print(b)
