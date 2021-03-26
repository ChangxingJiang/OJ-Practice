# LeetCode题解(0637)：计算二叉树的层平均值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/)（简单）

| 解法           | 时间复杂度 | 空间复杂度                 | 执行用时      |
| -------------- | ---------- | -------------------------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(M)$ : M为层节点数最大值 | 64ms (66.57%) |
| Ans 2 (Python) |            |                            |               |
| Ans 3 (Python) |            |                            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（广度优先遍历）：

```python
def averageOfLevels(self, root: TreeNode) -> List[float]:
    ans = []
    now_level = [root]
    while len(now_level) > 0:
        nums = []
        next_level = []
        for node in now_level:
            if node:
                nums.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        ans.append(sum(nums) / len(nums))
        now_level = next_level
    return ans
```