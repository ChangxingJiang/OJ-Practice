# LeetCode题解(0299)：猜数字游戏(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bulls-and-cows/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(n)       | O(n)       | 44ms (92.14%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表）：

```python
def getHint(self, secret: str, guess: str) -> str:
    s_map = {}
    g_map = {}
    bulls = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
        else:
            if secret[i] not in s_map:
                s_map[secret[i]] = 1
            else:
                s_map[secret[i]] += 1
            if guess[i] not in g_map:
                g_map[guess[i]] = 1
            else:
                g_map[guess[i]] += 1

    cows = 0
    for s in s_map:
        if s in g_map:
            cows += min(s_map[s], g_map[s])

    return str(bulls) + "A" + str(cows) + "B"
```