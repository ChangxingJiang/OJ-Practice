# LeetCode题解(1044)：最长重复子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-duplicate-substring/)（困难）

标签：哈希表、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时         |
| -------------- | ---------- | ---------- | ---------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 1340ms (100.00%) |
| Ans 2 (Python) |            |            |                  |
| Ans 3 (Python) |            |            |                  |

解法一：

```python
class Solution:
    _MOD = 2 ** 32

    def longestDupSubstring(self, S: str) -> str:
        def check(v):
            now = 0
            for i in range(v):
                now = (26 * now + nums[i]) % self._MOD

            count = {now}

            max_bit = pow(26, v, self._MOD)
            for i in range(size - v):
                now = (now * 26 - nums[i] * max_bit + nums[i + v]) % self._MOD
                if now in count:
                    return i + 1
                count.add(now)

            return -1

        size = len(S)
        nums = [ord(S[i]) - 97 for i in range(size)]

        start = -1
        left, right = 0, size
        while left < right:
            mid = (left + right) // 2
            res = check(mid)
            print(mid, ":", res)
            if res != -1:
                start = res
                left = mid + 1
            else:
                right = mid

        return S[start:start + left - 1] if start != -1 else ""
```