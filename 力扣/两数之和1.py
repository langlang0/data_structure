from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int):
        a = nums.copy()
        nums.sort()
        slow = 0
        fast = len(nums) - 1
        while slow < fast:
            if nums[slow] + nums[fast] < target:
                slow += 1
            elif nums[slow] + nums[fast] > target:
                fast -= 1
            else:
                if nums[slow] == nums[fast]:
                    return a.index(
                        nums[slow]), a.index(
                        nums[fast], a.index(
                            nums[slow]) + 1)
                else:
                    return a.index(nums[slow]), a.index(nums[fast])


class Solution1:
    def twoSum(self, nums: List[int], target: int):
        head = 0
        end = len(nums) - 1
        while head < end:
            sum = nums[head] + nums[end]
            if sum == target:
                print(nums[head], nums[end])
                head += 1
                end -= 1
            else:
                if sum < target:
                    head += 1
                else:
                    end -= 1


class Solution2:
    def twoSum(self, nums: List[int], target: int):
        nums_dict = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums_dict:
                return [nums_dict[temp], i]
            else:
                nums_dict[nums[i]] = i

class Solution3:
    def twoSum(self, nums: List[int], target: int):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

s = Solution2()
a = [9, 3, 2, 7]

print(s.twoSum(a, 5))
