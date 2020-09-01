# LeetCode题解(0848)：字母逐个移位转换(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shifting-letters/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 236ms (60.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（反向遍历）：

```python
class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        # 字符转换
        def shift(ch, n):
            return chr((ord(ch) - 97 + n) % 26 + 97)

        # 反向遍历字符串
        ans = []
        now = 0
        for i in range(len(shifts) - 1, -1, -1):
            now += shifts[i]
            ans.append(shift(S[i], now))

        # 反转生成结果
        return "".join(reversed(ans))
```