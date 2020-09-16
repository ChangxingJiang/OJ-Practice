# LeetCode题解(0367)：判断整数是否为完全平方数(Python)

## 题目内容

给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/valid-perfect-square

## 解法效率

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 40ms (72.32%) |
| Ans 2 (Python) | O(logn)    | O(1)       | 36ms (88.10%) |
| Ans 3 (Python) | --         | O(1)       | 40ms (72.32%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

### 解法一（不符合题意的sqrt解法）：

> 我们先用Python内置的pow方法做一个结果，仅作执行用时的参考。

```python
def isPerfectSquare(self, num: int) -> bool:
    return pow(num, 0.5) % 1 == 0
```

### 解法二（二分法求解）：

> 【思路】对于求平方根，我们很容易就想到了二分查找，不断在1和整数(num)之间二分取值(m)，比较其完全平方数(s)与当前整数(num)的大小。

```python
def isPerfectSquare(self, num: int) -> bool:
    left_index = 1
    right_index = num
    while left_index <= right_index:
        m = (left_index + right_index) // 2
        s = pow(m, 2)
        if s < num:
            left_index = m + 1
        elif s > num:
            right_index = m - 1
        else:
            return True
    else:
        return False
```

### 解法三（利用完全平方数各项的差为奇数等差数列）：

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