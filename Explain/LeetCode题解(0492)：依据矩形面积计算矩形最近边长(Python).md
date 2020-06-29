# LeetCode题解(0492)：依据矩形面积计算矩形最近边长(Python)

题目：[原题链接](https://leetcode-cn.com/problems/construct-the-rectangle/)（简单）

题目标签：

| 解法           | 时间复杂度    | 空间复杂度 | 执行用时        |
| -------------- | ------------- | ---------- | --------------- |
| Ans 1 (Python) | O(n)          | O(1)       | 2488ms (10.92%) |
| Ans 2 (Python) | $O(\sqrt{n})$ | O(1)       | 36ms (93.80%)   |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def constructRectangle(self, area: int) -> List[int]:
    c = pow(area, 0.5)
    l = w = int(c)  # l>w
    while l * w != area:
        if l * w < area:
            l += 1
        else:
            w -= 1
    return [l, w]
```

解法二（遍历解法）：

```python
def constructRectangle(self, area: int) -> List[int]:
    c = int(pow(area, 0.5))
    while area % c != 0:
        c -= 1
    else:
        return [c, area // c]
```

