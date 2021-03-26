# LeetCode题解(Offer35)：复制带随机指针的链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/)（中等）

标签：链表、链表-特殊链表、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 52ms (45.41%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（哈希表）：

```python
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        ans = node = Node(0)

        # 第一次遍历生成链表和哈希表
        now = head
        hashmap = {}
        while now:
            node.next = Node(now.val)
            hashmap[now] = node.next
            node = node.next
            now = now.next

        # 第二次遍历生成链表随机指针
        now = head
        node = ans.next
        while now:
            if now.random:
                node.random = hashmap[now.random]
            node = node.next
            now = now.next

        return ans.next
```