# LeetCode题解(1496)：判断路径是否相交(Python)

题目：[原题链接](https://leetcode-cn.com/problems/path-crossing/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 32ms (96.86%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（存储到过的位置）：

```python
def isPathCrossing(self, path: str) -> bool:
    orient = {
        "N": (0, 1),
        "S": (0, -1),
        "E": (1, 0),
        "W": (-1, 0),
    }

    x, y = 0, 0
    already = {(0, 0)}

    for p in path:
        o = orient[p]
        x += o[0]
        y += o[1]
        if (x, y) in already:
            return True
        already.add((x,y))
    else:
        return False
```