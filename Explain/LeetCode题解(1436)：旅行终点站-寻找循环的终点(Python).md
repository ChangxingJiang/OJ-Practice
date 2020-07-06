# LeetCode题解(1436)：旅行终点站-寻找循环的终点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/destination-city/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (83.01%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 36ms (94.12%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双集合）：

```python
def destCity(self, paths: List[List[str]]) -> str:
    maybe = set()
    wrong = set()
    for path in paths:
        wrong.add(path[0])
        maybe.add(path[1])
    return (maybe - wrong).pop()
```

解法二（增加跳出循环，提高效率）：

```python
def destCity(self, paths: List[List[str]]) -> str:
    paths = list(zip(*paths))
    wrong = set(paths[0])
    for path in paths[1]:
        if path not in wrong:
            return path
```