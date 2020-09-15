# LeetCode题解(0013)：将罗马数字转换为整数(Python)

题目：[题目链接](https://leetcode-cn.com/problems/roman-to-integer/)（简单）

标签：字符串、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 52ms (92.57%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 52ms (92.57%) |

解法一（观察发现，先直接统计总数；当发现小数出现在大数的左侧时，则减去两次小数）：

```python
def romanToInt(self, s: str) -> int:

    number = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    t = None  # 上一个字符
    ans = 0  # 数值总计
    for c in s:
        if t:
            if number[t] < number[c]:
                ans -= number[t] * 2
            ans += number[c]
        else:
            ans += number[c]
        t = c
    return ans
```

解法二（整理解法一代码）：

```python
def romanToInt(self, s: str) -> int:

    number = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    last = 0  # 上一个字符
    ans = 0  # 数值总计
    for ch in s:
        n = number[ch]
        ans += n
        if last < n:
            ans -= 2 * last
        last = n
    return ans
```

