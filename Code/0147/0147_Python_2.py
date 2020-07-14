from toolkit import ListNode


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 处理特殊情况
        if not head or not head.next:
            return head

        # 插入排序
        ans = ListNode(float("-inf"))
        last = ans
        node = head
        while node:
            # 寻找插入位置
            if last.val < node.val:
                point = node.next
                node.next = None
                last.next = node
                last = last.next
                node = point
            else:
                curr = ans
                while curr.next and curr.next.val < node.val:
                    curr = curr.next

                # 执行插入
                point = node.next
                node.next = curr.next
                curr.next = node
                node = point

        return ans.next


if __name__ == "__main__":
    print(Solution().insertionSortList(ListNode([4, 2, 1, 3])))  # 1->2->3->4
    print(Solution().insertionSortList(ListNode([-1, 5, 3, 4, 0])))  # -1->0->3->4->5
