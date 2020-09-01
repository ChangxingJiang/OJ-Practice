# LeetCode题解(0017)：九键手机按键的字母组合(Python)

题目：[原题链接](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)（中等）

标签：字符串、回溯算法

| 解法           | 时间复杂度   | 空间复杂度   | 执行用时      |
| -------------- | ------------ | ------------ | ------------- |
| Ans 1 (Python) | $O(3^N+4^M)$ | $O(3^N+4^M)$ | 32ms (95.50%) |
| Ans 2 (Python) | $O(3^N+4^M)$ | $O(3^N+4^M)$ | 32ms (95.50%) |
| Ans 3 (Python) |              |              |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（枚举法）：

```
def letterCombinations(self, digits: str) -> List[str]:
    phone = {"2": ["a", "b", "c"],
             "3": ["d", "e", "f"],
             "4": ["g", "h", "i"],
             "5": ["j", "k", "l"],
             "6": ["m", "n", "o"],
             "7": ["p", "q", "r", "s"],
             "8": ["t", "u", "v"],
             "9": ["w", "x", "y", "z"]}

    ans = [""]
    for d in digits:
        if d in phone:
            new = []
            for item in ans:
                for c in phone[d]:
                    new.append(item + c)
            ans = new

    return ans
```

解法二（不需要剪枝的回溯算法）：

> 测试用例中不包含字符1和字符0

```python
def letterCombinations(self, digits: str) -> List[str]:
    phone = {"2": ["a", "b", "c"],
             "3": ["d", "e", "f"],
             "4": ["g", "h", "i"],
             "5": ["j", "k", "l"],
             "6": ["m", "n", "o"],
             "7": ["p", "q", "r", "s"],
             "8": ["t", "u", "v"],
             "9": ["w", "x", "y", "z"]}

    def backtrack(now, next_digits):
        if not next_digits:
            ans.append(now)
        else:
            for d in phone[next_digits[0]]:
                backtrack(now + d, next_digits[1:])

    ans = []
    if digits:
        backtrack("", digits)
    return ans
```