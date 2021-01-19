# LeetCode题解(1093)：大样本统计(Python)

题目：[原题链接](https://leetcode-cn.com/problems/statistics-from-a-large-sample/)（中等）

标签：数学、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(256)$   | $O(256)$   | 52ms (78.26%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n1, n2, n3, n4, n5 = -1, -1, -1, -1, -1  # 最小值、最大值、平均值、中位数、众数
        _sum, _len = 0, 0
        most_common = 0
        for i in range(256):
            if n1 == -1 and count[i] > 0:
                n1 = i
            if count[i] > 0:
                n2 = i
            if count[i] > most_common:
                n5, most_common = i, count[i]
            _sum += count[i] * i
            _len += count[i]

        n3 = _sum / _len

        if _len == 1:
            n4 = n1
        elif _len == 2:
            n4 = (n1 + n2) / 2
        else:
            if _len % 2 == 0:
                k1, k2 = _len // 2, _len // 2 + 1
            else:
                k1 = k2 = _len // 2 + 1

            v1 = v2 = 0
            now = 0
            for i in range(256):
                now += count[i]
                if now >= k1 and v1 == 0:
                    v1 = i
                if now >= k2 and v2 == 0:
                    v2 = i

            n4 = (v1 + v2) / 2

        return [n1, n2, n3, n4, n5]
```

