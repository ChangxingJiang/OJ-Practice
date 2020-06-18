# LeetCode题解(0202)：判断整数是否为快乐数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/happy-number/)（简单）

| 解法           | 时间复杂度(n为运算次数) | 空间复杂度(n为运算次数) | 执行用时       |
| -------------- | ----------------------- | ----------------------- | -------------- |
| Ans 1 (Python) | O(n)                    | O(n)                    | 44ms (>73.40%) |
| Ans 2 (Python) | O(n)                    | O(1)                    | 44ms (>73.40%) |

上表中的n从开始运算到变为1的运算次数，或无限循环到第一次出现重复数字的运算次数。

| 解法           | 时间复杂度(n为数值) | 空间复杂度 | 执行用时       |
| -------------- | ------------------- | ---------- | -------------- |
| Ans 1 (Python) | O(logn)             | O(logn)    | 44ms (>73.40%) |
| Ans 2 (Python) | O(logn)             | O(1)       | 44ms (>73.40%) |

上表中的n为需要计算是否为快乐数的数值。

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（配合哈希表遍历）：

```python
def isHappy(self, n: int) -> bool:
    already = set()
    while n != 1:
        if n in already:
            return False
        already.add(n)
        n = sum([int(x) * int(x) for x in str(n)])
    return True
```

解法二（快慢指针法）：

```python
def isHappy(self, n: int) -> bool:
    fast = n
    slow = n
    while fast != 1 and slow != 1:
        fast = sum([int(x) * int(x) for x in str(fast)])
        fast = sum([int(x) * int(x) for x in str(fast)])
        slow = sum([int(x) * int(x) for x in str(slow)])
        if fast == slow and fast != 1:
            return False
    return True
```