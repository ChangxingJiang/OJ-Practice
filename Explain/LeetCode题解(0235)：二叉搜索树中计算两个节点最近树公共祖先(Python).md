# LeetCode题解(0235)：二叉搜索树中计算两个节点最近的公共祖先(Python)

题目：[原题链接](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | O(n)       | O(n)       | 128ms (>16.34%) |
| Ans 2 (Python) | O(logn)    | O(n)       | 92ms (>86.93%)  |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（不考虑二叉搜索树的性质，递归查找）：

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def helper(node):
        if not node:
            return 0, None
        find_num_left, find_left = helper(node.left)
        find_num_right, find_right = helper(node.right)
        find_num = 0
        if find_num_left == 2:
            return 2, find_left
        if find_num_right == 2:
            return 2, find_right
        if node.val == p.val or node.val == q.val:
            find_num += 1
        find_num += find_num_left + find_num_right
        if find_num == 2:
            return 2, node
        else:
            return find_num, None

    find_num, find_node = helper(root)
    if find_num == 2:
        return find_node
```

解法二（使用二拆搜索树的性质迭代）：

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    while root:
        if p.val > root.val and q.val > root.val:
            root = root.right
            continue
        if p.val < root.val and q.val < root.val:
            root = root.left
            continue
        else:
            return root
```