# LeetCode题解(0067)：字符串表示的二进制求和(Python）

题目：[题目链接](https://leetcode-cn.com/problems/add-binary/)（简单）

标签：字符串、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| :------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 44ms (65.80%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 40ms (82.92%) |
| Ans 3 (Python) | $O(N)$     | $O(N)$     | 36ms (94.93%) |

解法一（捣蛋方法）：

```python
def addBinary(self, a: str, b: str) -> str:
    a = int(a, 2)
    b = int(b, 2)
    s = a + b
    s = bin(s)
    return str(s).replace("0b", "")
```

解法二：

```python
def addBinary(self, a: str, b: str) -> str:
    a = [int(t) for t in a]
    b = [int(t) for t in b]

    len_a = len(a)
    len_b = len(b)

    s = []
    add = 0
    for i in range(1, max(len_a, len_b) + 1):
        c = add
        if i <= len_a:
            c += a[-i]
        if i <= len_b:
            c += b[-i]
        if c == 0:
            s.insert(0, "0")
            add = 0
        elif c == 1:
            s.insert(0, "1")
            add = 0
        elif c == 2:
            s.insert(0, "0")
            add = 1
        else:
            s.insert(0, "1")
            add = 1
    if add == 1:
        s.insert(0, "1")
    return "".join(s)
```

解法三（优化解法二）：

```python
def addBinary(self, a: str, b: str) -> str:
    a = [int(t) for t in a]
    b = [int(t) for t in b]

    N1 = len(a)
    N2 = len(b)

    ans = []
    now = 0
    for i in range(1, max(N1, N2) + 1):
        # 计算当期数量
        c = now
        if i <= N1:
            c += a[-i]
        if i <= N2:
            c += b[-i]

        # 计算当前位及进位
        if c == 0:
            ans.append("0")
            now = 0
        elif c == 1:
            ans.append("1")
            now = 0
        elif c == 2:
            ans.append("0")
            now = 1
        else:
            ans.append("1")
            now = 1
    if now == 1:
        ans.append("1")
    return "".join(ans[::-1])
```