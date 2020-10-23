def threesum(nums: list, target):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sums = nums[left] + nums[right] + nums[i]
            if sums < target:
                left += 1
            elif sums > target:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
    return res


if __name__ == '__main__':
    a = [-4, -1, -1, 0, 1, 2]
    print(threesum(a, 0))
