from toolkit import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 处理特殊情况
        if not head:
            return None

        # 将链表的队尾的指针指向链表的队头
        size = 1
        node = head
        while node.next:
            node = node.next
            size += 1
        node.next = head

        # 计算新的队头位置
        k = k % size

        # 将新的队尾指向空，并返回新的队头
        node = head
        for _ in range(size - k - 1):
            node = node.next
        ans = node.next
        node.next = None

        return ans


if __name__ == "__main__":
    print(Solution().rotateRight(ListNode([1, 2, 3, 4, 5]), k=2))  # 4->5->1->2->3
    print(Solution().rotateRight(ListNode([0, 1, 2]), k=4))  # 2->0->1
