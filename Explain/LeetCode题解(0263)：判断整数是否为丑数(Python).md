# LeetCode题解(0263)：判断整数是否为丑数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ugly-number/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(logn)    | O(1)       | 48ms (43.23%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（迭代除质因子，若丑数最后一定剩余1）：

```python
def isUgly(self, num: int) -> bool:
    if num <=0:
        return False
    while num > 1:
        if num % 2 == 0:
            num /= 2
        elif num % 3 == 0:
            num /= 3
        elif num % 5 == 0:
            num /= 5
        else:
            return False
    else:
        return True
```