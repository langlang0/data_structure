from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1  # 记录慢指针指向的值的相同个数
        slow = 0
        fast = 1
        num = 0    # 记录删除掉的元素个数
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                count += 1
                if count == 2:
                    slow += 1
                    nums[slow] = nums[fast]
                    num += 1     # 删掉后,计数加一,方便输出列表
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
                count = 1
        return nums[:len(nums) - num]


if __name__ == '__main__':
    s = Solution()
    a = [1, 1, 1, 2, 2, 3]
    b = s.removeDuplicates(a)
    print(b)
