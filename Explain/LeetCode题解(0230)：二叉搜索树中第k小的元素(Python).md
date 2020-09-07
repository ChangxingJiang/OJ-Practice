# LeetCode题解(0230)：寻找二叉搜索树中第k小的元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/)（中等）

标签：树、二叉树、二叉搜索树、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(H+k)$   | $O(H)$     | 64ms (78.10%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（迭代的中序遍历）：

```python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = [root]
        while stack:
            if node := stack[-1]:
                stack.append(node.left)
            else:
                stack.pop()
                if not stack:
                    break
                node = stack.pop()
                stack.append(node.right)

                # 检查是否已经找到第k小的结果
                if k > 1:
                    k -= 1
                else:
                    return node.val
```