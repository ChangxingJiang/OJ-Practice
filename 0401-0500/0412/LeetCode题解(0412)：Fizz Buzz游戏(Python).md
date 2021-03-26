# LeetCode题解(0412)：Fizz Buzz游戏(Python)

题目：[原题链接](https://leetcode-cn.com/problems/fizz-buzz/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(n)       | O(1)       | 52ms (82.27%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def fizzBuzz(self, n: int) -> List[str]:
    def helper(t):
        r3 = t % 3
        r5 = t % 5
        if r3 == 0 and r5 == 0:
            return "FizzBuzz"
        elif r3 == 0:
            return "Fizz"
        elif r5 == 0:
            return "Buzz"
        else:
            return str(t)

    return [helper(i) for i in range(1, n + 1)]
```