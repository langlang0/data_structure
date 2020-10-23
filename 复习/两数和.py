from typing import List


def twoSum(nums: List[int], target: int):
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right:
        sums = nums[left] + nums[right]
        if sums < target:
            left += 1
        elif sums > target:
            right -= 1
        else:
            return [left, right]


def twoSum1(nums: List[int], target: int):
    dic = {}
    for i in range(len(nums)):
        sums = target - nums[i]
        if sums not in dic:
            dic[nums[i]] = i
        else:
            return [dic[sums], i]


def twoSum2(nums: List[int], target: int):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


if __name__ == '__main__':
    a = [9, 3, 2, 7]
    print(twoSum(a, 5))
