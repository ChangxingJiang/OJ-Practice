# LeetCode题解(0904)：水果成篮(Python)

题目：[原题链接](https://leetcode-cn.com/problems/fruit-into-baskets/)（中等）

标签：数组、双指针、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 1160ms (17.70%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ans = 0

        l, r = 0, 0
        window = collections.Counter()
        while r < len(tree):
            window[tree[r]] += 1
            while len(window) > 2:
                window[tree[l]] -= 1
                if window[tree[l]] == 0:
                    window.pop(tree[l])
                l += 1
            ans = max(ans, r - l + 1)
            r += 1

        return ans
```

