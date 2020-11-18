# LeetCode题解(1569)：将子数组重新排序得到同一个二叉查找树的方案数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/)（困难）

标签：树、二叉树、二叉树-二叉搜索树、数学、记忆化递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 192ms (59.24%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（记忆化递归）：

```python
def comb(n, m):
    return math.factorial(n) // (math.factorial(n - m) * math.factorial(m))


class Solution:
    def numOfWays(self, nums: List[int]) -> int:

        @functools.lru_cache(None)
        def count(num_lst):
            # 只有1个或2个结点的树，是没有重排方法的
            if len(num_lst) == 1 or len(num_lst) == 2:
                return 1

            # 计算左右子树
            root = num_lst[0]
            left = tuple([num for num in num_lst if num < root])
            right = tuple([num for num in num_lst if num > root])

            # 处理只有单侧子树的情况
            if not left:
                return count(right)
            if not right:
                return count(left)

            # 计算左右子树结点数量
            left_num, right_num = len(left), len(right)
            if left_num == 1 and right_num == 1:
                return 2

            # 计算左右子树可以变化程度
            left_change = count(left)
            right_change = count(right)

            # 计算总变化数
            total_num = left_num + right_num
            total_change = comb(total_num, left_num) * left_change * right_change

            print(root, left, right, "->", (total_num * (total_num - 1) / 2), left_change, right_change, "->",
                  total_change)

            return total_change

        ans = (count(tuple(nums)) - 1)
        return ans % (10 ** 9 + 7) if ans else 0
```

