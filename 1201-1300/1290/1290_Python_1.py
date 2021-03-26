from toolkit import ListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = ans << 1
            ans = ans ^ head.val
            head = head.next
        return ans


if __name__ == "__main__":
    print(Solution().getDecimalValue(ListNode([1, 0, 1])))  # 5
    print(Solution().getDecimalValue(ListNode([0])))  # 0
    print(Solution().getDecimalValue(ListNode([1])))  # 1
    print(Solution().getDecimalValue(ListNode([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])))  # 18880
    print(Solution().getDecimalValue(ListNode([0, 0])))  # 0
