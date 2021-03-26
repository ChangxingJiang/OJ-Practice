# LeetCode题解(1647)：字符频次唯一的最小删除次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-deletions-to-make-character-frequencies-unique/)（中等）

标签：贪心算法、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 132ms (78.44%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minDeletions(self, s: str) -> int:
        count = collections.Counter(s)
        num_list = list(sorted(count.values(), reverse=True))

        ans = 0

        now = num_list[0]
        for i in range(1, len(num_list)):
            if num_list[i] >= now:
                if now > 0:
                    ans += (num_list[i] - (now - 1))
                    now -= 1
                else:
                    ans += num_list[i]
            else:
                now = num_list[i]

        return ans
```

