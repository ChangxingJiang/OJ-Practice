# LeetCode题解(Offer57II)：和为目标值的连续正整数序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/)（简单）

标签：数学、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 52ms (89.99%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ans = []
        for n in range(2, int((target * 2) ** 0.5 + 1)):
            a, b = divmod(target, n)
            c, d = divmod(int(n * (n - 1) / 2), n)
            if b == d:
                ans.append([a - c + i for i in range(n)])
        return ans[::-1]
```