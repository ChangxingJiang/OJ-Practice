# LeetCode题解(0482)：密钥格式化(Python)

题目：[原题链接](https://leetcode-cn.com/problems/license-key-formatting/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(n)       | O(n)       | 68ms (66.75%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（反向遍历）：

```python
def licenseKeyFormatting(self, S: str, K: int) -> str:
    S = S.upper()
    ans = []
    now = ""
    for s in S[::-1]:
        if s.isalnum():
            now += s
            if len(now) == K:
                ans.append(now[::-1])
                now = ""
    else:
        if len(now) > 0:
            ans.append(now[::-1])
    return "-".join(ans[::-1])
```

