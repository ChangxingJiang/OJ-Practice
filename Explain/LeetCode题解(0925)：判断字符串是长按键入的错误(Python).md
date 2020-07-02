# LeetCode题解(0925)：判断字符串是长按键入的错误(Python)

题目：[原题链接](https://leetcode-cn.com/problems/long-pressed-name/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N+K)$   | $O(1)$     | 44ms (56.90%) |
| Ans 2 (Python) | $O(N+K)$   | $O(N+K)$   | 48ms (32.38%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双指针）：

```python
def isLongPressedName(self, name: str, typed: str) -> bool:
    idx = 0
    for i in range(len(typed)):
        if idx < len(name) and typed[i] == name[idx]:
            idx += 1
        else:
            if i == 0 or typed[i] != name[idx - 1]:
                return False
    return idx == len(name)
```

解法二（按块比较长度）：

```python
def isLongPressedName(self, name: str, typed: str) -> bool:
    g1 = [(k, len(list(group))) for k, group in itertools.groupby(name)]
    g2 = [(k, len(list(group))) for k, group in itertools.groupby(typed)]
    if len(g1) != len(g2):
        return False
    return all(k1 == k2 and v1 <= v2 for (k1, v1), (k2, v2) in zip(g1, g2))
```