# LeetCode题解(0880)：计算超长解码字符串中索引处的值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/decoded-string-at-index/)（中等）

标签：字符串、逆向法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(K)$     | $O(K)$     | 超出时间限制  |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 32ms (97.06%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（直接记录字符串）：

```python
def decodeAtIndex(self, S: str, K: int) -> str:
    stack = []
    idx = 0
    size = len(S)
    while idx < size and len(stack) < K:
        if S[idx].isalpha():
            stack.append(S[idx])
        else:
            num = int(S[idx])
            now = len(stack)
            for _ in range(num - 1):
                for i in range(now):
                    stack.append(stack[i])
                    if len(stack) >= K:
                        break
        idx += 1
    return stack[K - 1]
```

解法二：

```python
def decodeAtIndex(self, S: str, K: int) -> str:
    # 统计最终解码字符串长度
    size = 0
    for ch in S:
        if ch.isdigit():
            size *= int(ch)
        else:
            size += 1

    # 不断逆向取模简化索引
    for ch in reversed(S):
        K %= size
        if K == 0 and ch.isalpha():
            return ch

        if ch.isdigit():
            size /= int(ch)
        else:
            size -= 1
```