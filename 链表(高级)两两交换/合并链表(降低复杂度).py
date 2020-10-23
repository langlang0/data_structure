class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node({self.val})"


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:              # 当l1为空链表时,输出l2
            return l2
        elif l2 is None:            # 当l2为空链表时,输出l1
            return l1
        elif l1.val < l2.val:       # 当l1的val值小于l2的val值时,将l1所在链设置为主链,否则l1为添加链
            prev = l1               # prev为两链中的最小结点
            add = l2                # add为要插入到主链上的结点
            out = l1                # out为输出链的头部
        else:
            prev = l2
            add = l1
            out = l2

        while add:                          # 当添加值不为空时,进行添加操作
            add_next = add.next             # 记录添加值的下一个值
            if prev.next is None:           # 当主链上的当前值的下一值为空时,将添加链整体连接到主链上,并结束循环
                prev.next = add
                break
            else:                           # 当主链上的当前值的下一值不为空,进行一下操作
                curr = prev.next            # 记录当前结点的下一结点,当前结点已保证小于添加结点
                if curr.val >= add.val:     # 当当前结点的下一结点大于等于添加结点时,将添加结点插入到当前结点的下一位
                    add.next = curr
                    prev.next = add
                    prev = prev.next        # 将当前结点向后移动一位
                    add = add_next
                else:                       # 当当前结点的下一结点小于添加结点时,将当前结点和当前结点的下一结点的指针向后移动一位
                    prev = curr
                    curr = curr.next
        return out


def output(node):
    while node:
        print(node.val, end=" ")
        node = node.next


if __name__ == '__main__':
    a1 = ListNode(-9)
    a2 = ListNode(3)
    b1 = ListNode(5)
    b2 = ListNode(7)

    a1.next = a2
    b1.next = b2

    s = Solution()
    print(s.mergeTwoLists(a1, b1))
    output(a1)
