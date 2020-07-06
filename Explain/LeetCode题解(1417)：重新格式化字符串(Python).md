# LeetCode题解(1417)：重新格式化字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reformat-the-string/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms（93.57%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def reformat(self, s: str) -> str:
    alphas = []
    nums = []
    for c in s:
        if c.isalpha():
            alphas.append(c)
        else:
            nums.append(c)

    if abs(len(alphas) - len(nums)) > 1:
        return ""

    ans = ""
    if len(alphas) < len(nums):
        for i in range(len(alphas)):
            ans += nums[i] + alphas[i]
        else:
            ans += nums[-1]
        return ans
    elif len(alphas) > len(nums):
        for i in range(len(nums)):
            ans += alphas[i] + nums[i]
        else:
            ans += alphas[-1]
    else:
        for i in range(len(nums)):
            ans += alphas[i] + nums[i]

    return ans
```