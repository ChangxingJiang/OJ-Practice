# LeetCode题解(面试17.18)：最短超串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shortest-supersequence-lcci/)（中等）

标签：滑动窗口、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(B+S)$   | $O(S+B)$   | 140ms (84.30%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        set_small = set(small)
        s1, s2 = len(big), len(small)
        count = collections.Counter()

        ans_idx, ans_val = [], float("inf")

        now = 0
        left = right = 0
        while right < s1:
            while right < s1 and now < s2:
                if big[right] in set_small:
                    if count[big[right]] == 0:
                        now += 1
                    count[big[right]] += 1
                right += 1

            # print(left, right, count)

            if now == s2:
                while left < right and (big[left] not in set_small or count[big[left]] > 1):
                    if big[left] in set_small:
                        count[big[left]] -= 1
                    left += 1

                if right - left < ans_val:
                    ans_idx, ans_val = [left, right - 1], right - left

                while left < right and now == s2:
                    if big[left] in set_small:
                        count[big[left]] -= 1
                        if count[big[left]] == 0:
                            now -= 1
                    left += 1

        return ans_idx
```