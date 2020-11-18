from LeetTool import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        i1 = i2 = head

        # 快慢针寻找环
        while i2.next and i2.next.next:
            i2 = i2.next.next
            i1 = i1.next
            if i1 == i2:
                break
        else:
            return None

        # 双指针寻找入环交点
        i3 = head
        while i1 != i3:
            i1 = i1.next
            i3 = i3.next

        return i1


if __name__ == "__main__":
    pass
