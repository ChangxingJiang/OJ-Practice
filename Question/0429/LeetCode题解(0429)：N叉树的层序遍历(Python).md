# LeetCode题解(0429)：实现N叉树的层序遍历(Python)

题目：[原题链接](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/)（中等）

标签：树、N叉树、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 64ms (75.06%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 处理特殊情况
        if not root:
            return []

        # 处理一般情况
        ans = []
        now_node = [root]
        while now_node:
            now_val = []
            next_node = []
            for node in now_node:
                now_val.append(node.val)
                if node.children:
                    for child in node.children:
                        next_node.append(child)
            ans.append(now_val)
            now_node = next_node

        return ans
```