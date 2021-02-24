# LeetCode题解(LCP23)：魔术排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/er94lq/)（中等）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 52ms (68.42%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isMagic(self, target: List[int]) -> bool:
        n = len(target)

        # 生成初始状态
        cards = [i for i in range(2, n + 1, 2)] + [i for i in range(1, n + 1, 2)]

        # 计算k值
        k = 0
        for j in range(n):
            if cards[j] == target[j]:
                k += 1
            else:
                break

        if k == 0:
            return False

        if k == n:
            return True

        # 情景模拟
        i = k
        while i < n:
            change = [cards[j] for j in range(k + 1, n - i + k, 2)] + [cards[j] for j in range(k, n - i + k, 2)]
            # print(cards, "->", change)
            for j in range(min(k, n - i)):
                if change[j] != target[i + j]:
                    return False
            cards = change
            i += k

        return True
```

