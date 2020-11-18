# LeetCode题解(1620)：网络信号最好的坐标(Python)

题目：[原题链接](https://leetcode-cn.com/problems/coordinate-with-maximum-network-quality/)（中等）

标签：几何、贪心算法

| 解法           | 时间复杂度  | 空间复杂度 | 执行用时    |
| -------------- | ----------- | ---------- | ----------- |
| Ans 1 (Python) | $O(50^2×T)$ | $O(1)$     | 3000ms(20%) |
| Ans 2 (Python) |             |            |             |
| Ans 3 (Python) |             |            |             |

解法一：

```python
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        ans, ans_power = [0, 0], 0
        for i in range(51):
            for j in range(51):
                power = 0
                for x, y, q in towers:
                    d = pow((x - i) ** 2 + (y - j) ** 2, 0.5)
                    if d <= radius:
                        power += math.floor(q / (1 + d))
                print(i, j, ":", power)
                if power > ans_power:
                    ans, ans_power = [i, j], power
        return ans
```