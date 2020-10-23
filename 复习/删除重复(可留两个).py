from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        count = 1
        while fast < len(nums):
            if count == 2:
                fast += 1
                count = 1
            else:
                if nums[slow] == nums[fast]:
                    count += 1
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow +1


if __name__ == '__main__':
    s = Solution()
    a = [1,2,3,4,4,4,5]
    print(s.removeDuplicates(a))