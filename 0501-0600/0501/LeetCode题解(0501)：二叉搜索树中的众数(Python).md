# LeetCode题解(0501)：二叉搜索树中的众数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(n)       | O(n)       | 68ms (76.96%) |
| Ans 2 (Python) | O(n)       | O(n)       | 68ms (76.96%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力递归）：

```python
def findMode(self, root: TreeNode) -> List[int]:
    if not root:
        return []

    hashmap = {}

    def helper(node):
        if node:
            if node.val in hashmap:
                hashmap[node.val] += 1
            else:
                hashmap[node.val] = 1
            return helper(node.left), helper(node.right)

    helper(root)
    maximum = max(hashmap.values())

    ans = []
    for key, value in hashmap.items():
        if value == maximum:
            ans.append(key)

    return ans
```

解法二（中序遍历二叉搜索树相当于遍历有序数组，双指针解法）：

```python
def __init__(self):
    self.max_counter = 0
    self._now = None
    self.counter = 0

def findMode(self, root: TreeNode) -> List[int]:

    res = []

    def helper(node):
        if not node:
            return None

        helper(node.left)

        if node.val == self._now:
            self.counter += 1
        else:
            self.counter = 0
            self._now = node.val

        if self.counter > self.max_counter:
            self.max_counter = self.counter
            res.clear()
            res.append(node.val)
        elif self.counter == self.max_counter:
            res.append(node.val)

        helper(node.right)

    helper(root)

    return res
```