# LeetCode题解(0653)：计算二叉搜索树中和为目标值的两结点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 135ms (16.84%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 100ms (60.84%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（中序遍历为数组处理）：

```python
def findTarget(self, root: TreeNode, k: int) -> bool:
    def helper(node):
        if not node:
            return []
        return helper(node.left) + [node.val] + helper(node.right)

    nums = helper(root)

    print(nums)

    hashmap = []

    for n in nums:
        if k - n not in hashmap:
            hashmap.append(n)
        else:
            return True
    else:
        return False
```

解法二（直接遍历二叉树）：

```python
def findTarget(self, root: TreeNode, k: int) -> bool:

    hashmap = []

    def helper(node):
        if node:
            if (k - node.val) in hashmap:
                return True
            hashmap.append(node.val)
            return helper(node.left) or helper(node.right)
        else:
            return False

    return helper(root)
```