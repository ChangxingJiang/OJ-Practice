from toolkit import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 计算l1的长度
        size1 = 0
        node1 = l1
        while node1:
            node1 = node1.next
            size1 += 1
        node1 = l1

        # 计算l2的长度
        size2 = 0
        node2 = l2
        while node2:
            node2 = node2.next
            size2 += 1
        node2 = l2

        maximum = max(size1, size2)

        ans = node = ListNode(0)
        stack = [node]
        for i in range(maximum, 0, -1):
            value = 0
            if size1 >= i:
                value += node1.val
                node1 = node1.next
            if size2 >= i:
                value += node2.val
                node2 = node2.next

            if value >= 10:
                for j in range(len(stack) - 1, -1, -1):
                    stack[j].val += 1
                    if stack[j].val == 10:
                        stack[j].val = 0
                    else:
                        break

            node.next = ListNode(value % 10)
            node = node.next
            stack.append(node)

        if ans.val:
            return ans
        else:
            return ans.next


if __name__ == "__main__":
    print(Solution().addTwoNumbers(ListNode([7, 2, 4, 3]), ListNode([5, 6, 4])))  # 7->8->0->7
    print(Solution().addTwoNumbers(ListNode([5]), ListNode([5])))  # 1->0
    print(Solution().addTwoNumbers(ListNode([9, 9]), ListNode([1])))  # 1->0->0
