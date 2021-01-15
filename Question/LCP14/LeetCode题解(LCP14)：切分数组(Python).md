# LeetCode题解(LCP14)：切分数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/qie-fen-shu-zu/)（困难）

标签：动态规划、哈希表

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时        |
| -------------- | ------------ | ---------- | --------------- |
| Ans 1 (Python) | $O(NlogM+M)$ | $O(M)$     | 1380ms (60.46%) |
| Ans 2 (Python) |              |            |                 |
| Ans 3 (Python) |              |            |                 |

解法一：

```python
# 计算每个数的最小质因子
_MAX = 10 ** 6
_FACTORS = [1 for _ in range(_MAX + 1)]
v = 2
while v <= _MAX:
    times = v
    while times * v <= _MAX:
        if _FACTORS[times * v] == 1:
            _FACTORS[times * v] = v
        times += 1

    v += 1
    while v <= _MAX:
        if _FACTORS[v] == 1:
            break
        v += 1


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        # 生成结果
        size = len(nums)
        dp = {}

        x = nums[0]
        while True:
            if _FACTORS[x] == 1:
                dp[x] = 1
                break
            dp[_FACTORS[x]] = 1
            x //= _FACTORS[x]

        last = 1
        for i in range(1, size):
            x = nums[i]

            now = float("inf")
            while True:
                if _FACTORS[x] == 1:
                    dp[x] = min(dp.get(x, float("inf")), last + 1)
                    now = min(now, dp[x])
                    break
                dp[_FACTORS[x]] = min(dp.get(_FACTORS[x], float("inf")), last + 1)
                now = min(now, dp[_FACTORS[x]])
                x //= _FACTORS[x]

            last = now

        return last
```

