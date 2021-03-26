# LeetCode题解(0945)：使数组唯一的最小增量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/)（中等）

标签：数组、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 320ms (98.61%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = collections.Counter(A)

        ans = 0
        last, waiting = -1, 0
        for now in sorted(count):
            if waiting > 0:
                diff = now - last - 1
                while diff > 0 and waiting > 0:
                    waiting -= 1
                    diff -= 1
                    ans += waiting
            waiting += count[now] - 1
            last = now

            ans += waiting

        while waiting:
            waiting -= 1
            ans += waiting

        return ans
```

