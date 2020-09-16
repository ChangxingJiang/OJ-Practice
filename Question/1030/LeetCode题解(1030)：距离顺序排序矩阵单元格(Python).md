# LeetCode题解(1030)：距离顺序排序矩阵单元格(Python)

题目：[原题链接](https://leetcode-cn.com/problems/matrix-cells-in-distance-order/)（简单）

| 解法           | 时间复杂度       | 空间复杂度 | 执行用时       |
| -------------- | ---------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(R×Clog(R×C))$ | $O(R×C)$   | 212ms (32.52%) |
| Ans 2 (Python) | $O(R×Clog(R×C))$ | $O(R×C)$   | 172ms (91.44%) |
| Ans 3 (Python) |                  |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（自定义排序）：

```python
def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    ans = []
    for i in range(R):
        for j in range(C):
            ans.append([i, j])

    ans.sort(key=lambda p: abs(p[0] - r0) + abs(p[1] - c0))

    return ans
```

解法二：

```python
def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    ans = {}
    for i in range(R):
        for j in range(C):
            distance = abs(i - r0) + abs(j - c0)
            if distance not in ans:
                ans[distance] = [[i, j]]
            else:
                ans[distance].append([i, j])

    res = []
    for key in sorted(ans.keys()):
        res.extend(ans[key])

    return res
```