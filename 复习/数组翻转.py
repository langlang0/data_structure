def reverse(nums: list):
    if len(nums) <= 1:
        return nums
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


if __name__ == '__main__':
    a = [1]
    print(reverse(a))
