# LeetCode题解(1806)：还原排列的最少操作步数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/)（中等）

标签：贪心算法、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (96.90%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        if n == 2:
            return 1

        # 判断数字1的位置
        ans = 1
        now = 2
        while now != 1:
            if now < n // 2:
                now *= 2
                ans += 1
            else:
                now = (now - n // 2) * 2 + 1
                ans += 1
        return ans
```

