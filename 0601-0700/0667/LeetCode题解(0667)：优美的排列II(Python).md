# LeetCode题解(0667)：优美的排列II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/beautiful-arrangement-ii/)（中等）

标签：数组、脑筋急转弯

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 60ms (56.80%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = [1]
        i1, i2 = 2, k + 1
        for i in range(1, k + 1):
            if i % 2 == 1:
                ans.append(i2)
                i2 -= 1
            else:
                ans.append(i1)
                i1 += 1
        ans += [i for i in range(k + 2, n + 1)]
        return ans
```

