def flag(nums: list):
    start, i, end = 0, 0, len(nums) - 1
    while i <= end:
        if nums[i] == 0:
            nums[start], nums[i] = nums[i], nums[start]
            start += 1
        if nums[i] == 2:
            nums[end], nums[i] = nums[i], nums[end]
            end -= 1
            i -= 1
        i += 1
    return nums


a = [1, 2, 0]
print(flag(a))
