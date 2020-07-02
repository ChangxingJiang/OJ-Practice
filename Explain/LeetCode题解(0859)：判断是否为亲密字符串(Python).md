# LeetCode题解(0859)：判断是否为亲密字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/buddy-strings/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms  (83.03%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 40ms  (83.03%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def buddyStrings(self, A: str, B: str) -> bool:
    if len(A) != len(B):
        return False

    differ = []
    for i in range(len(A)):
        if A[i] != B[i]:
            differ.append(i)

    if len(differ) == 2:
        return A[differ[0]] == B[differ[1]] and A[differ[1]] == B[differ[0]]
    elif len(differ) == 0:
        return len(set(A)) < len(A)
    else:
        return False
```

解法二（整理解法一的逻辑）：

```python
def buddyStrings(self, A: str, B: str) -> bool:
    if A == B:
        return len(set(A)) < len(A)
    else:
        if len(A) != len(B):
            return False
        differ = []
        for i in range(len(A)):
            if A[i] != B[i]:
                differ.append(i)
        return len(differ) == 2 and A[differ[0]] == B[differ[1]] and A[differ[1]] == B[differ[0]]
```