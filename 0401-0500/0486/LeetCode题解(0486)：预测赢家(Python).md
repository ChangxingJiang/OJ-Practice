# LeetCode题解(0486)：预测赢家(Python)

题目：[原题链接](https://leetcode-cn.com/problems/predict-the-winner/)（中等）

标签：递归、极小化极大、动态规划、动态规划-状态表格

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(2^N)$   | $O(N)$     | 3640ms (7.96%) |
| Ans 2 (Python) | $O(2^N)$   | $O(2^N)$   | 36ms (96.31%)  |
| Ans 3 (Python) | $O(N^2)$   | $O(N^2)$   | 44ms (73.40%)  |

解法一（情景模拟+递归）：

```python
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def f(left, right):
            """递归函数"""
            # 处理剩下1个数的情况
            if left == right:
                return nums[left]
            # 处理剩下2个数的情况
            elif left == right - 1:
                return max(nums[left], nums[right])
            # 处理剩下3+个数的情况
            else:
                # 当前拿的数以及被对手拿去最合理的数之后的给自己剩下的数
                return max(nums[left] + min(f(left + 1, right - 1), f(left + 2, right)),
                           nums[right] + min(f(left, right - 2), f(left + 1, right - 1)))

        total_1 = f(0, len(nums) - 1)
        total_2 = sum(nums) - total_1

        return total_1 >= total_2
```

解法二（优化解法一）：

```python
import functools
from typing import List


class Solution:

    def PredictTheWinner(self, nums: List[int]) -> bool:
        @functools.lru_cache(None)
        def f(left, right):
            """递归函数"""
            # 处理剩下1个数的情况
            if left == right:
                return nums[left]
            # 处理剩下2个数的情况
            elif left == right - 1:
                return max(nums[left], nums[right])
            # 处理剩下3+个数的情况
            else:
                # 当前拿的数以及被对手拿去最合理的数之后的给自己剩下的数
                return max(nums[left] + min(f(left + 1, right - 1), f(left + 2, right)),
                           nums[right] + min(f(left, right - 2), f(left + 1, right - 1)))

        total_1 = f(0, len(nums) - 1)
        total_2 = sum(nums) - total_1

        return total_1 >= total_2
```

解法三（动态规划）：

```python
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)

        # 定义状态矩阵（记录以j开头，i结尾的字符串中，先手和后手的玩家的分数差）
        dp = [[0] * N for _ in range(N)]

        # 填写状态矩阵对角线（即只有一个数的情况）
        for i in range(N):
            dp[i][i] = nums[i]

        # 填写状态矩阵其他位置（取走第一个数和取走最后一个数中结果的最大值）
        for i in range(1, N):
            for j in range(i - 1, -1, -1):
                dp[i][j] = max(nums[i] - dp[i - 1][j], nums[j] - dp[i][j + 1])

        # 返回最终结果
        return dp[N - 1][0] >= 0
```