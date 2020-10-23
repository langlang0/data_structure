from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mins = abs(nums[0] + nums[1] + nums[2] - target)
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if abs(sums - target) < mins:
                    mins = abs(sums - target)
                    res = sums
                if sums < target:
                    left += 1
                elif sums > target:
                    right -= 1
                else:
                    return sums
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
