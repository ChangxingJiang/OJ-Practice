# LeetCode题解(0447)：在平面上众多点中寻找距离相同的点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-boomerangs/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | O(n^2)     | O(n)       | 1300ms (79.66%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def numberOfBoomerangs(self, points: List[List[int]]) -> int:
    ans = 0
    for p1 in points:
        hashmap = {}
        for p2 in points:
            s = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
            if s in hashmap:
                hashmap[s] += 1
            else:
                hashmap[s] = 1

        for key, value in hashmap.items():
            if key != 0:
                ans += value * (value - 1)

    return ans
```