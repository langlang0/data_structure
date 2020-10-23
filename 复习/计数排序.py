def countsort(nums: list):
    maxNum = max(nums)
    countList = [0] * (maxNum + 1)

    for i in range(len(nums)):
        countList[nums[i]] += 1

    res = []
    for j in range(len(countList)):
        res += ([j] * countList[j])
    return res


print(countsort([3,3,4,1,2,3,5,6,3,2,1,1]))