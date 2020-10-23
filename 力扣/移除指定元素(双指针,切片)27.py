from typing import List


class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0    # 指针,当前位置元素
        num = 0     # 记录非当前值元素个数
        while slow < len(nums):
            if nums[slow] == val:
                nums[slow:] = nums[slow + 1:]
            else:
                slow += 1
                num += 1
        return num


class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                fast += 1
                slow += 1
        return slow


a = [1, 2, 3, 4, 5, 5, 5, 6, 7]
b = Solution2()

print(b.removeElement(a, 5))
