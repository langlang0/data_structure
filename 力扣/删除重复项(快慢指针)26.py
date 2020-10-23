from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]):
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow + 1, nums[:slow + 1]


a = [1, 1, 1, 1, 2, 3, 4, 5]
b = Solution()
print(b.removeDuplicates(a))
