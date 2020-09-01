# LeetCode题解(1496)：依据移动方向判断路径是否相交(Python)

题目：[原题链接](https://leetcode-cn.com/problems/path-crossing/)（简单）

标签：字符串、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 32ms (96.86%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

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