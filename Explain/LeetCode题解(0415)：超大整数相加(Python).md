# LeetCode题解(0415)：字符串表示的大数相加(Python)

题目：[原题链接](https://leetcode-cn.com/problems/add-strings/)（简单）

标签：字符串、数学

相关题目：0043

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N+M)$   | $O(N+M)$   | 60ms (52.23%) |
| Ans 2 (Python) | $O(N+M)$   | $O(N+M)$   | 52ms (79.49%) |
| Ans 3 (Python) | --         | --         | 36ms (99.36%) |

解法一：

```python
def addStrings(self, num1: str, num2: str) -> str:
    num1 = num1.zfill(len(num2))
    num2 = num2.zfill(len(num1))
    carry = 0
    ans = []
    for i in range(1, len(num1) + 1):
        n1 = int(num1[-i])
        n2 = int(num2[-i])
        n = n1 + n2 + carry
        ans.append(str(n % 10))
        carry = n // 10
    if carry == 1:
        ans.append("1")
    ans.reverse()
    return "".join(ans)
```

解法二：

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        N1, N2 = len(num1), len(num2)
        N = max(N1, N2) + 1
        now = 0
        ans = []
        for i in range(1, N + 1):
            now += int(num1[-i]) if i <= N1 else 0
            now += int(num2[-i]) if i <= N2 else 0
            now, n = divmod(now, 10)
            if i != N or now != 0 or n != 0:
                ans.append(str(n))
        return "".join(reversed(ans))
```

解法三（不符合题意的最快解法）：

![LeetCode题解(0415)：截图1](LeetCode题解(0415)：截图1.png)

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))
```