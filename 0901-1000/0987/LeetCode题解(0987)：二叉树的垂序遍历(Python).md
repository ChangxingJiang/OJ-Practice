# LeetCode题解(0987)：实现二叉树的垂序遍历(Python)

题目：[原题链接](https://leetcode-cn.com/problems/vertical-order-traversal-of-a-binary-tree/)（中等）

标签：树、二叉树、深度优先搜索、广度优先搜索、哈希表

| 解法           | 时间复杂度                              | 空间复杂度 | 执行用时      |
| -------------- | --------------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN+HlogH)$ ： 其中H为二叉树的深度 | $O(N)$     | 52ms (21.62%) |
| Ans 2 (Python) | $O(NlogN)$                              | $O(N)$     | 44ms (72.64%) |
| Ans 3 (Python) |                                         |            |               |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.ans = collections.defaultdict(list)

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def dfs(node, idx, level):
            if node:
                self.ans[idx].append((node.val, level))
                if node.left:
                    dfs(node.left, idx - 1, level + 1)
                if node.right:
                    dfs(node.right, idx + 1, level + 1)

        dfs(root, 0, 0)
        ans = []
        for k in sorted(self.ans.keys()):
            ans.append([elem[0] for elem in sorted(self.ans[k], key=lambda x: (x[1], x[0]))])
        return ans
```

解法二（广度优先搜索）：

```python
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        ans = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            tmp_ans = collections.defaultdict(list)
            for _ in range(len(queue)):
                node, idx = queue.popleft()
                tmp_ans[idx].append(node.val)
                if node.left:
                    queue.append((node.left, idx - 1))
                if node.right:
                    queue.append((node.right, idx + 1))
            for k, v in tmp_ans.items():
                ans[k].extend(sorted(v))

        return [ans[k] for k in sorted(ans.keys())]
```