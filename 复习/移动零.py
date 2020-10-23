from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        for i in range(slow,len(nums)):
            nums[i] = 0
        return nums


if __name__ == '__main__':
    s = Solution()
    a = [0,1,0,3]
    print(s.moveZeroes(a))
