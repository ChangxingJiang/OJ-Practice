# LeetCode题解(0367)：判断是否为完全平方数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/valid-perfect-square/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 40ms (72.32%) |
| Ans 2 (Python) | O(logn)    | O(1)       | 36ms (88.10%) |
| Ans 3 (Python) | --         | O(1)       | 40ms (72.32%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（不符合题意的sqrt解法）：

```python
def isPerfectSquare(self, num: int) -> bool:
    return pow(num, 0.5) % 1 == 0
```

解法二（二分法求解）：

```python
def isPerfectSquare(self, num: int) -> bool:
    left_index = 1
    right_index = num
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        s = pow(mid_index, 2)
        if s < num:
            left_index = mid_index + 1
        elif s > num:
            right_index = mid_index - 1
        else:
            return True
    else:
        return False
```

解法三（利用完全平方数各项的差为奇数等差数列）：

```python
def isPerfectSquare(self, num: int) -> bool:
    k = 1
    n = 0
    while n <= num:
        n += k
        k += 2
        if n == num:
            return True
    else:
        return False
```