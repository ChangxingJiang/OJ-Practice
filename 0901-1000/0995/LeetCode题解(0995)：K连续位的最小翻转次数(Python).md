# LeetCode题解(0995)：K连续位的最小翻转次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips/)（困难）

标签：贪心算法、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 908ms (53.33%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minKBitFlips(self, A: List[int], k: int) -> int:
        # 处理K=1的特殊情况
        if k == 1:
            return A.count(0)

        size = len(A)
        array = [0] * (size + 1)
        ans = 0
        now = 0
        for i in range(size):
            now ^= array[i]
            # print(i, ":", now, "->", now ^ A[i], array)
            if i < size - k + 1:
                if now ^ A[i] == 0:
                    now ^= 1
                    array[i + k] = 1
                    ans += 1
            else:
                if now ^ A[i] == 0:
                    return -1

        return ans
```

