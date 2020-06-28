# LeetCode题解(0401)：推断二进制手表中所有可能的时间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-watch/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(total)   | O(n)       | 48ms (46.94%) |
| Ans 2 (Python) | O(10^n)    | O(10^n)    | 44ms (66.82%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力法）：

```python
def readBinaryWatch(self, num: int) -> List[str]:
    ans = []
    for h in range(12):
        for m in range(60):
            if bin(h).count("1") + bin(m).count("1") == num:
                ans.append("%d:%02d" % (h, m))
    return ans
```

解法二（回溯法）：

```python
def readBinaryWatch(self, num: int) -> List[str]:
    hour = [1, 2, 4, 8]
    minute = [1, 2, 4, 8, 16, 32]

    ans = []

    def helper(n, index, status):
        if n == 0:
            h = sum([i * j for i, j in zip(hour, status[:4])])
            m = sum([i * j for i, j in zip(minute, status[4:])])
            if h < 12 and m < 60:
                ans.append("%d:%02d" % (h, m))
        else:
            for i in range(index, 10):
                status[i] = 1
                helper(n - 1, i + 1, status)
                status[i] = 0

    helper(num, 0, [0] * 10)

    return ans
```