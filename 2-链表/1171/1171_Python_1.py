from toolkit import ListNode


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        pass


if __name__ == "__main__":
    print(Solution().removeZeroSumSublists(ListNode([1, 2, -3, 3, 1])))  # [3,1]
    print(Solution().removeZeroSumSublists(ListNode([1, 2, 3, -3, 4])))  # [1,2,4]
    print(Solution().removeZeroSumSublists(ListNode([1, 2, 3, -3, -2])))  # [1]
