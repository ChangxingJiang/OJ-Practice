# LeetCode题解(1524)：和为奇数的子数组数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-sub-arrays-with-odd-sum/)（中等）

标签：数组、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 272ms (27.03%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    _MOD = 10 ** 9 + 7

    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n0, n1, total = 1, 0, 0
        for n in arr:
            total += n
            if total % 2 == 1:
                ans += n0
            else:
                ans += n1  # 前面有n1-1个，自己是1个
            ans %= self._MOD
            if total % 2 == 0:
                n0 += 1
            else:
                n1 += 1
        return ans
```

