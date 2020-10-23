def bucketSort(nums: list):
    maxnum = max(nums)
    minnum = min(nums)
    d = maxnum - minnum

    bucket_num = len(nums)
    count_list = []
    for i in range(bucket_num):
        count_list.append([])

    for i in range(len(nums)):
        num = int((nums[i] - minnum) * (bucket_num - 1) / d)
        bucket = count_list[num]
        bucket.append(nums[i])

    for i in range(len(count_list)):
        count_list[i].sort()

    sort_nums = []
    for i in count_list:
        for j in i:
            sort_nums.append(j)
    return sort_nums



