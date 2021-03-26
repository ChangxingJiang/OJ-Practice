# LeetCode题解(Offer32III)：锯齿形层次遍历二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/)（中等）

标签：树、二叉树、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (64.14%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = collections.deque([root])
        reverse = False
        while queue:
            now_val = []
            for _ in range(len(queue)):
                node = queue.popleft()
                now_val.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if reverse:
                ans.append(now_val[::-1])
            else:
                ans.append(now_val)

            reverse = not reverse

        return ans
```