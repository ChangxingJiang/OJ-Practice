from toolkit import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        stack2 = []
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        ans = None
        carry = 0
        while stack1 or stack2 or carry > 0:
            n1 = stack1.pop() if stack1 else 0
            n2 = stack2.pop() if stack2 else 0
            value = n1 + n2 + carry
            carry = value // 10
            node = ListNode(value % 10)
            node.next = ans
            ans = node

        return ans


if __name__ == "__main__":
    print(Solution().addTwoNumbers(ListNode([7, 2, 4, 3]), ListNode([5, 6, 4])))  # 7->8->0->7
    print(Solution().addTwoNumbers(ListNode([5]), ListNode([5])))  # 1->0
    print(Solution().addTwoNumbers(ListNode([9, 9]), ListNode([1])))  # 1->0->0
