# LeetCode题解(0148)：常数级空间复杂度排序链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sort-list/)（中等）

标签：链表、链表-双指针、排序、排序-归并排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(logN)$  | 428ms (5.14%)  |
| Ans 2 (Python) | $O(NlogN)$ | $O(1)$     | 264ms (32.29%) |
| Ans 3 (Python) | $O(NlogN)$ | $O(1)$     | 264ms (32.29%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（递归的归并排序）：

```python
class Solution:
    # 排序两个排序链表
    @staticmethod
    def helper(head1, head2):
        ans = node = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                node.next = ListNode(head1.val)
                node = node.next
                head1 = head1.next
            else:
                node.next = ListNode(head2.val)
                node = node.next
                head2 = head2.next

        if head1 or head2:
            node.next = head1 or head2

        return ans.next

    def sortList(self, head: ListNode) -> ListNode:
        # 处理特殊情况
        if not head or not head.next:
            return head

        # 获取链表中点
        slow = fast = head
        fast = fast.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        node2 = slow.next
        slow.next = None
        node1 = head

        return self.helper(self.sortList(node1), self.sortList(node2))
```

解法二（由下向上的归并排序）：

```python
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
```

解法三（优化的解法二）：

```python
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
                # 获取第一段链表的头并检查长度
                n = ps
                node1 = node
                while n > 0 and node:
                    node = node.next
                    n -= 1
                if n > 0:
                    break

                # 获取两段链表的头
                n = ps
                node2 = node
                while n > 0 and node:
                    node = node.next
                    n -= 1

                # 计算两段链表的长度
                size1 = ps
                size2 = ps - n

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
```