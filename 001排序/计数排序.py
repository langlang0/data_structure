from typing import List


def countsort(nums: List):
    # 列表去重
    ilist = []
    for i in nums:
        if i not in ilist:
            ilist.append(i)
    # 列表排序
    ilist.sort()
    # 新建字典,接收值及对应个数
    dic = {}
    for i in ilist:
        dic[i] = nums.count(i)
    # 新建空列表,遍历字典,追加元素
    res = []
    for k, v in dic.items():
        for i in range(v):
            res.append(k)
    return res


def count_sort(nums):
    max_value = max(nums)
    count_arr = [0] * (max_value + 1)

    for i in range(len(nums)):
        count_arr[nums[i]] += 1

    sort_arr = []
    for i in range(len(count_arr)):
        for j in range(count_arr[i]):
            sort_arr.append(i)
    return sort_arr


a = [1, 2, 3, 4, 3, 2, 3, 2, 1, 2, 4, 512, 12, 4, 5]

print(countsort(a))

