from toolkit import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 计算链表长度
        size, node = 0, head
        while node:
            node = node.next
            size += 1

        # 定义处理变量
        ans = ListNode(0)
        ans.next = head

        # 归并排序
        ps = 1
        while ps < size:
            pre = ans
            node = ans.next
            for i in range(0, size, ps * 2):

                if size - i <= ps:
                    break

                # 获取两段链表的头
                node1 = node
                for _ in range(ps):
                    node = node.next
                node2 = node
                for _ in range(ps):
                    if node:
                        node = node.next

                # 计算两段链表的长度
                size1 = ps
                size2 = min(ps, size - i - ps)

                # 排序两个排序链表
                while size1 > 0 and size2 > 0:
                    if node1.val < node2.val:
                        point = node1.next
                        pre.next = node1
                        node1 = point
                        size1 -= 1
                    else:
                        point = node2.next
                        pre.next = node2
                        node2 = point
                        size2 -= 1
                    pre = pre.next

                if size1 > 0:
                    pre.next = node1
                if size2 > 0:
                    pre.next = node2

                while size1 > 0 or size2 > 0:
                    pre = pre.next
                    size1 -= 1
                    size2 -= 1

                pre.next = node

            ps *= 2

        return ans.next


if __name__ == "__main__":
    print(Solution().sortList(ListNode([4, 2, 1, 3])))  # 1->2->3->4
    print(Solution().sortList(ListNode([-1, 5, 3, 4, 0])))  # -1->0->3->4->5
