# LeetCode题解(0812)：在集合中取出三个点，组成最大面积三角形(Python)

题目：[原题链接](https://leetcode-cn.com/problems/largest-triangle-area/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(1)$     | 608ms (28.63%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

### 解法一（暴力解法）

> **【思路】**
>
> 根据题意，我们最先想到的就是遍历所有可能的三个点的组合，找出能够组成的最大三角形面积。
>
> 在具体的实现中，我们使用海伦公式，依据三角形三边长求三角形面积。实现如下：

```
def largestTriangleArea(self, points: List[List[int]]) -> float:
    def distance(pp1, pp2):
        return pow(pow(pp1[0] - pp2[0], 2) + pow(pp1[1] - pp2[1], 2), 0.5)

    ans = 0
    for i1 in range(len(points)):
        p1 = points[i1]
        for i2 in range(i1 + 1, len(points)):
            p2 = points[i2]
            for i3 in range(i2 + 1, len(points)):
                p3 = points[i3]
                a = distance(p1, p2)
                b = distance(p1, p3)
                c = distance(p2, p3)
                p = (a + b + c) / 2
                t = p * (p - a) * (p - b) * (p - c)
                if t > 0:
                    s = pow(p * (p - a) * (p - b) * (p - c), 0.5)  # 海伦公式求面积
                    ans = max(ans, s)
    return round(ans, 2)
```