from typing import List


class Solution:
    def search(self, nums: List[int]) -> List[int]:
        slow = 0
        fast = len(nums) - 1
        while slow < fast:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
            fast -= 1
        return nums


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7]
    s = Solution()
    print(s.search(a))
