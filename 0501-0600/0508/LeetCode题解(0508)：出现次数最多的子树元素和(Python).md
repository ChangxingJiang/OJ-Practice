# LeetCode题解(0508)：出现次数最多的子树元素和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/most-frequent-subtree-sum/)（中等）

标签：树、二叉树、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 60ms (81.10%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.count = collections.Counter()

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def recursor(node):
            if not node:
                return 0
            left_val = recursor(node.left)
            right_val = recursor(node.right)
            node_val = node.val + left_val + right_val
            self.count[node_val] += 1
            return node_val

        recursor(root)

        ans = []
        max_val = None

        for node in self.count.most_common():
            if max_val is None:
                max_val = node[1]
                ans.append(node[0])
            elif node[1] == max_val:
                ans.append(node[0])
            else:
                break

        return ans
```