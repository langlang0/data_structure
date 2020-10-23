from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow + 1


if __name__ == '__main__':
    s = Solution()
    a = [1, 1, 2, 2, 3, 4, 5, 5, 5]
    print(s.removeDuplicates(a))
