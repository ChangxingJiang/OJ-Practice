# LeetCode题解(0860)：柠檬水找零(Python)

题目：[原题链接](https://leetcode-cn.com/problems/lemonade-change/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 168ms (87.14%) |
| Ans 2 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（模拟情景）：

```python
def lemonadeChange(self, bills: List[int]) -> bool:
    five = 0  # 5美元的数量
    ten = 0  # 10美元的数量

    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five < 1:
                return False
            else:
                five -= 1
                ten += 1
        else:
            if ten < 1:
                if five < 3:
                    return False
                else:
                    five -= 3
            else:
                if five < 1:
                    return False
                else:
                    five -= 1
                    ten -= 1
    else:
        return True
```