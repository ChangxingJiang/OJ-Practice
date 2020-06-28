# LeetCode题解(0443)：字符串压缩(Python)

题目：[原题链接](https://leetcode-cn.com/problems/string-compression/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(n)       | O(n)       | 92ms (20.75%) |
| Ans 2 (Python) | O(n)       | O(n)       | 68ms (89.76%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def compress(self, chars: List[str]) -> int:
    now = None
    num = 0
    ans = ""
    for c in chars:
        if c == now:
            num += 1
        else:
            if now is not None:
                if num > 1:
                    ans += now + str(num)
                else:
                    ans += now
            now = c
            num = 1
    else:
        if num > 1:
            ans += now + str(num)
        else:
            ans += now
    chars.clear()
    chars.extend(list(ans))
    return len(ans)
```

解法二：

```python
def compress(self, chars: List[str]) -> int:
    if len(chars) == 0:
        return 0
    now = chars[-1]
    num = 1
    for i in range(len(chars) - 2, - 1, -1):
        if chars[i] == now:
            num += 1
            chars.pop(i + 1)
        else:
            if num > 1:
                for j in str(num)[::-1]:
                    chars.insert(i + 2, j)
            now = chars[i]
            num = 1
    else:
        if num > 1:
            for j in str(num)[::-1]:
                chars.insert(1, j)
    return len(chars)
```