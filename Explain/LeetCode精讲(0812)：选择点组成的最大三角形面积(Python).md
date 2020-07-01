# LeetCode精讲(0812)：在集合中取出三个点，组成最大面积三角形(Python)

## 题目内容

给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。

**示例：**

```
输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
输出: 2
解释: 
这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
```

**注意：**

* 3 <= points.length <= 50.
* 不存在重复的点。
*  -50 <= points[i][j] <= 50.
* 结果误差值在 10^-6 以内都认为是正确答案。

> 来源：力扣（LeetCode）
> 
> 链接：https://leetcode-cn.com/problems/largest-triangle-area

## 解法效率

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(1)$     | 608ms (28.63%) |
| Ans 2 (Python) | $O(N^3)$   | $O(1)$     | 128ms (91.98%) |
| Ans 3 (Python) | $O(N^3)$   | $O(1)$     | 100ms (96.18%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

### 解法一（海伦公式求面积）

根据题意，我们最先想到的就是遍历所有可能的三个点的组合，找出能够组成的最大三角形面积。

在具体的实现中，我们使用海伦公式求三角形面积。实现如下：

```python
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

### 解法二（顶点坐标求面积）

**【思路】**

我们发现海伦公式在求解三角形面积时，需要先计算三边长，再由三边长计算三角形面积，在计算过程中，需要3次开方运算，效率较低。

因为我们已知三角形的顶点坐标，所以我们可以直接使用如下公式。

> 已知三角形的三个顶点坐标A(x1,y1)、B(x2,y2)、C(x3,y3)，则三角形面积为：
>
> S=abs(x1\*(y2-y3) + x2\*(y3-y1) + x3\*(y1-y2))/2

实现如下：

```python
def largestTriangleArea(self, points: List[List[int]]) -> float:
    ans = 0
    for i1 in range(len(points)):
        [x1, y1] = points[i1]
        for i2 in range(i1 + 1, len(points)):
            [x2, y2] = points[i2]
            for i3 in range(i2 + 1, len(points)):
                [x3, y3] = points[i3]
                s = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))) / 2
                ans = max(ans, s)
    return ans
```

### 解法三（使用组合）

我们使用itertools中的组合函数，让我们的代码更优雅。

```python
def largestTriangleArea(self, points: List[List[int]]) -> float:
    return max(abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
               for (x1, y1), (x2, y2), (x3, y3) in itertools.combinations(points, 3)) / 2
```

