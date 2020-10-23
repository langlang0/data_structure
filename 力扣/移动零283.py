from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        fast = 0
        slow = 0
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow] = nums[fast]
                fast += 1
                slow += 1
        for i in range(slow, len(nums)):
            nums[i] = 0
        return nums


a = Solution()
b = [1, 0, 2, 0, 3]
print(a.moveZeroes(b))
