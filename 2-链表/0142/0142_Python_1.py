from toolkit import ListNode, build_ListNode_with_pos


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        pass


if __name__ == "__main__":
    print(Solution().detectCycle(build_ListNode_with_pos([3, 2, 0, -4], pos=1)))  # 2
    print(Solution().detectCycle(build_ListNode_with_pos([1, 2], pos=0)))  # 1
    print(Solution().detectCycle(build_ListNode_with_pos([1], pos=-1)))  # -1
