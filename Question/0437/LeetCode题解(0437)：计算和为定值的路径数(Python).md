# LeetCode题解(0437)：计算和为定值的路径数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/path-sum-iii/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | O(n^2)     | O(n)       | 7844ms (5.04%) |
| Ans 2 (Python) | O(nlogn)   | O(n^2)     | 204ms (79.27%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（遍历树的同时遍历路径）：

```python
def pathSum(self, root: TreeNode, s: int) -> int:
    self.ans = 0

    def helper(node, source):
        # 处理树末端的情况
        if node is None:
            return

        # 计算当前路径
        source.append(node.val)

        # 判断路径是否等于目标值
        for i in range(len(source)):
            if sum(source[i:]) == s:
                self.ans += 1

        # 继续检查子节点
        if node.left is not None:
            helper(node.left, copy.deepcopy(source))
        if node.right is not None:
            helper(node.right, copy.deepcopy(source))

    helper(root, [])

    return self.ans
```

解法二（路径和列表）：

```python
def pathSum(self, root: TreeNode, s: int) -> int:
    def helper(node, sums):
        # 处理树末端的情况
        if node is None:
            return 0

        # 统计当前路径和列表
        sums = [t + node.val for t in sums] + [node.val]

        # 继续检查子节点
        return sums.count(s) + helper(node.left, sums) + helper(node.right, sums)

    return helper(root, [])
```