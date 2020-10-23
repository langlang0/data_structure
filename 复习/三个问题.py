def move(nums: list, target):
    fast = 0
    while fast < len(nums):
        if nums[fast] == target:
            nums[fast:] = nums[fast + 1:]
        else:
            fast += 1
    return nums


def moves(nums: list, target):
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] == target:
            fast += 1
        else:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    return nums[:slow]


def movezero(nums: list):
    fast = 0
    count = 0
    while fast < len(nums) - count:
        if nums[fast] == 0:
            nums[fast:len(nums) - count] = nums[fast + 1:]
            nums[-1] = 0
            count += 1
        else:
            fast += 1
    return nums


if __name__ == '__main__':
    # a = [1, 3, 5, 6, 8, 9, 3]
    # print(moves(a, 3))
    b = [0,3,2,4,1,0,4,0]
    print(movezero(b))




