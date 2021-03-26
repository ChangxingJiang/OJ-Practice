# LeetCode题解(0708)：循环有序列表的插入(Python)

题目：[原题链接](https://leetcode-cn.com/problems/insert-into-a-sorted-circular-linked-list/)（中等）

标签：链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 52ms (36.36%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # 处理链表为空的情况
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        # 处理链表不为空的情况
        node = head
        already = False  # 是否已转过一周

        while True:
            # 处理只有一个元素的链表的情况
            if node == node.next:
                new = Node(insertVal, node.next)
                node.next = new
                break

            # 处理在链表中的情况
            elif node.val <= node.next.val:
                if node.val <= insertVal <= node.next.val:
                    new = Node(insertVal, node.next)
                    node.next = new
                    break
                else:
                    node = node.next

            # 处理到达链表末尾的情况
            else:
                if already:
                    new = Node(insertVal, node.next)
                    node.next = new
                    break
                else:
                    node = node.next

            if node == head:
                if not already:
                    already = True
                else:
                    new = Node(insertVal, node.next)
                    node.next = new
                    break

        return head
```