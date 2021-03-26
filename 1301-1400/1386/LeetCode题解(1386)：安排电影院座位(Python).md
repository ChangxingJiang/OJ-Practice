# LeetCode题解(1386)：安排电影院座位(Python)

题目：[原题链接](https://leetcode-cn.com/problems/cinema-seat-allocation/)（中等）

标签：贪心算法、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(R)$     | $O(R)$     | 144ms (41.56%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        info = collections.defaultdict(list)
        for i, j in reservedSeats:
            info[i].append(j)

        ans = (10 // 4) * (n - len(info))  # 计算空行数量

        for i in info:
            choice1 = {2, 3, 4, 5}
            choice2 = {4, 5, 6, 7}
            choice3 = {6, 7, 8, 9}
            b1, b2, b3 = True, True, True
            for j in info[i]:
                if j in choice1:
                    b1 = False
                if j in choice2:
                    b2 = False
                if j in choice3:
                    b3 = False
            if b1 and b3:
                ans += 2
            elif b1 or b2 or b3:
                ans += 1

        return ans
```

