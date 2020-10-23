from typing import List


class Solution:
    def search(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] == val:
            return left
        if nums[right] == val:
            return right
        while left < right - 1:
            number = (left + right + 1) // 2
            if nums[number] == val:
                return number
            if nums[number] < val:
                left = number
            if nums[number] > val:
                right = number


a = [-1, 0, 3, 5, 9, 12]
s = Solution()
print(s.search(a, 2))
