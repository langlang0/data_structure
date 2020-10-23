from typing import List


# 超出时间限制
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] > nums[right]:
                    count += 1
                if left + 1 == right:
                    left = i + 1
                    right -= 1
                else:
                    left += 1
        return count


# 超出时间限制
class Solution1:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        i = 0
        left = 1
        right = len(nums) - 1
        while True:
            if i + 2 > len(nums) - 1:
                return count
            if left == right:
                i += 1
                left = i + 1
                right = len(nums) - 1
                continue
            if nums[i] + nums[left] > nums[right]:
                count += 1
            if left + 1 == right:
                left = i + 1
                right -= 1
            else:
                left += 1


# 已通过力扣    对撞指针,控制最大的边长,对撞另外两边
class Solution2:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(2,len(nums)):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count


a = [2, 2, 3, 4]
s = Solution2()
print(s.triangleNumber(a))
