def insertSort(nums: list):
    if len(nums) <= 1:
        return nums
    for right in range(len(nums)):
        target = nums[right]
        for left in range(right):
            if nums[left] > target:
                nums[left + 1:right + 1] = nums[left:right]
                nums[left] = target
                break
        print(f"第{right + 1}轮排序结果: {nums}")


def insertsort(nums:list):
    if len(nums) <= 1:
        return nums
    for right in range(len(nums)):
        targht = nums[right]
        for left in range(right):
            if nums[left] > targht:
                nums[left + 1:right + 1] = nums[left:right]
                nums[left] = targht
                break


a = [2, 5, 7, 1, 9, 3, 4]
insertSort(a)
print(a)
