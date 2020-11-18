# LeetCode题解(面试04.03)：特定深度节点链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/list-of-depth-lcci/)（中等）

标签：树、二叉树、广度优先搜索、链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (74.54%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        ans = []
        tree_nodes = collections.deque([tree])
        while tree_nodes:
            head = node = ListNode(0)
            for i in range(len(tree_nodes)):
                now = tree_nodes.popleft()
                if now.left:
                    tree_nodes.append(now.left)
                if now.right:
                    tree_nodes.append(now.right)
                node.next = ListNode(now.val)
                node = node.next
            ans.append(head.next)

        return ans
```

