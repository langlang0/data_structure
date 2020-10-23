from typing import List


class Solution:
    def threeSum(self, nums: List[int]):
        output = []
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    a = [nums[i], nums[left], nums[right]]
                    if a not in output:
                        output.append(a)
                    elif nums[left] == nums[right]:
                        break
                    else:
                        left += 1
                        right -= 1
        return output


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for m in range(j + 1, len(nums)):
                    sums = nums[i] + nums[j] + nums[m]
                    list_out = sorted([nums[i], nums[j], nums[m]])
                    if sums == 0 and list_out not in output:
                        output.append(list_out)
        return output


class Solution2:
    def threeSum(self, nums: List[int]):
        output = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    output += [[nums[i], nums[left], nums[right]]]
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return output


# a = [-2, -1, -1, 0, 1, 2, 3]
# s = Solution()
# print(s.threeSum(a))


a = [1,23,3]
a[6] = 99
a[5] = 98
a[4] = 97
a[3] = 96

print(a)