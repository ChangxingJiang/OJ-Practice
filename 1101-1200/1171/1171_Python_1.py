from toolkit import ListNode


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        # 将链表转换为数组
        values = []
        while head:
            values.append(head.val)
            head = head.next

        # 删除总和为0的连续结点
        for k in range(len(values), 0, -1):
            while True:
                for i in range(len(values) - k + 1):
                    if sum(values[i:i + k]) == 0:
                        values = values[:i] + values[i + k:]
                        break
                else:
                    break

        head = node = ListNode(0)
        for v in values:
            node.next = ListNode(v)
            node = node.next
        return head.next


if __name__ == "__main__":
    print(Solution().removeZeroSumSublists(ListNode([1, 2, -3, 3, 1])))  # [3,1]
    print(Solution().removeZeroSumSublists(ListNode([1, 2, 3, -3, 4])))  # [1,2,4]
    print(Solution().removeZeroSumSublists(ListNode([1, 2, 3, -3, -2])))  # [1]
