# LeetCode题解(Offer32I)：实现二叉树的层序遍历(不分层输出)(Python)

题目：[原题链接](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)（中等）

标签：树、二叉树、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (61.95%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ans = []
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            ans.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ans
```

