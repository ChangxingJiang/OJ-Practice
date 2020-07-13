from toolkit import ListNode, build_ListNode_with_pos


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 快慢针判断是否有环
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        # 找到入口
        node1 = slow
        node2 = head
        while node1 != node2:
            node1 = node1.next
            node2 = node2.next

        return node1


if __name__ == "__main__":
    print(Solution().detectCycle(build_ListNode_with_pos([3, 2, 0, -4], pos=1)).val)  # 2
    print(Solution().detectCycle(build_ListNode_with_pos([1, 2], pos=0)).val)  # 1
    print(Solution().detectCycle(build_ListNode_with_pos([1], pos=-1)).val)  # -1
