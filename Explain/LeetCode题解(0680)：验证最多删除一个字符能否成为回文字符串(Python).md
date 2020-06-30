# LeetCode题解(0680)：验证最多删除一个字符能否成为回文字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/valid-palindrome-ii/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 236ms (16.06%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 200ms (30.88%) |
| Ans 3 (Python) | $O(N)$     | $O(1)$     | 196ms (35.48%) |
| Ans 4 (Python) | --         | $O(N)$     | 60ms (99.65%)  |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双指针遍历，出现错误则将两种修改情况重新遍历）：

```python
def __init__(self):
    self.wrong = 0

def validPalindrome(self, s: str) -> bool:
    idx1 = 0
    idx2 = len(s) - 1
    while idx1 <= idx2:
        if s[idx1] != s[idx2]:
            self.wrong += 1
            if self.wrong >= 2:
                return False

            sf1 = s[:idx1] + s[idx1 + 1:]
            sf2 = s[:idx2] + s[idx2 + 1:]
            return self.validPalindrome(sf1) or self.validPalindrome(sf2)
        idx1 += 1
        idx2 -= 1
    return True
```

解法二（解法一的优化，出现错误只遍历两种修改情况尚未遍历的部分）：

```python
def __init__(self):
    self.wrong = 0

def validPalindrome(self, s: str) -> bool:
    idx1 = 0
    idx2 = len(s) - 1
    while idx1 <= idx2:
        if s[idx1] != s[idx2]:
            self.wrong += 1
            if self.wrong >= 2:
                return False

            sf1 = s[idx1 + 1:idx2 + 1]
            sf2 = s[idx1:idx2]
            return self.validPalindrome(sf1) or self.validPalindrome(sf2)
        idx1 += 1
        idx2 -= 1
    return True
```

解法三（不再生成新的子串）：

```python
def validPalindrome(self, s: str) -> bool:
    def helper(i1, i2):
        while i1 < i2:
            if s[i1] != s[i2]:
                return False
            i1 += 1
            i2 -= 1
        return True

    idx1, idx2 = 0, len(s) - 1
    while idx1 <= idx2:
        if s[idx1] != s[idx2]:
            return helper(idx1 + 1, idx2) or helper(idx1, idx2 - 1)
        idx1 += 1
        idx2 -= 1
    return True
```

解法四（直接比较字符串）：

![LeetCode题解(0680)：截图1.png](LeetCode题解(0680)：截图1.png)

```python
def validPalindrome(self, s: str) -> bool:
    size = len(s)
    r = s[::-1]
    if s == r:
        return True
    for i in range(size):
        if r[i] != s[i]:
            new_s = s[:i] + s[i + 1:]
            new_r = r[:size - i - 1] + r[size - i:]
            if new_s == new_r:
                return True
            new_s = s[:size - i - 1] + s[size - i:]
            new_r = r[:i] + r[i + 1:]
            if new_s == new_r:
                return True
            break
    return False
```