# LeetCode题解(0385)：实现迷你嵌套列表语法分析器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/mini-parser/)（中等）

标签：字符串、分治算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 56ms (97.40%) |
| Ans 2 (Python) | $O(N)$     | $O(logN)$  | 80ms (38.02%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（最不要脸的方法）：

```python
def deserialize(self, s: str) -> NestedInteger:
    return NestedInteger(eval(s))
```

解法二（分治算法）：

```python
def deserialize(self, s: str) -> NestedInteger:
    # 处理只是一个整数的情况
    if s[0] != "[":
        return NestedInteger(int(s))

    # 处理一个空列表的情况
    elif s == "[]":
        return NestedInteger()

    # 处理一个列表的情况
    else:
        ans = NestedInteger()
        s = s[1:-1]
        num = 0
        last = 0
        for i in range(len(s)):
            if s[i] == "," and num == 0:
                ans.add(self.deserialize(s[last:i]))
                last = i + 1
            elif s[i] == "[":
                num += 1
            elif s[i] == "]":
                num -= 1
        ans.add(self.deserialize(s[last:]))
        return ans
```