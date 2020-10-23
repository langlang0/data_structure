from typing import List


class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] == val:
                nums[fast:] = nums[fast + 1:]
            else:
                fast += 1
        return nums


if __name__ == '__main__':
    s = Solution1()
    a = [1,2,3,4,5,5,5,6,7]
    print(s.removeElement(a,2))