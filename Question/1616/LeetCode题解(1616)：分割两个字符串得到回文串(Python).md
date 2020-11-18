# LeetCode题解(1616)：分割两个字符串得到回文串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/split-two-strings-to-make-palindrome/)（中等）

标签：字符串、贪心算法、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(A+B)$   | $O(1)$     | 152ms (38%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        size = len(a)

        # 第1种拼接情况
        cut = False
        right = True
        for i in range(size // 2):
            left, right = i, size - i - 1
            if not cut:
                if a[left] != b[right]:
                    if b[left] == b[right]:
                        cut = True
                    else:
                        right = False
                        break
            else:
                if b[left] != b[right]:
                    right = False
                    break
        if right:
            print("第1种拼接")
            return True

        # 第2种拼接情况
        cut = False
        right = True
        for i in range(size // 2):
            left, right = i, size - i - 1
            if not cut:
                if a[left] != b[right]:
                    if a[left] == a[right]:
                        cut = True
                    else:
                        right = False
                        break
            else:
                if a[left] != a[right]:
                    right = False
                    break
        if right:
            print("第2种拼接")
            return True

        # 第3种拼接情况
        cut = False
        right = True
        for i in range(size // 2):
            left, right = i, size - i - 1
            if not cut:
                if b[left] != a[right]:
                    if a[left] == a[right]:
                        cut = True
                    else:
                        right = False
                        break
            else:
                if a[left] != a[right]:
                    right = False
                    break
        if right:
            print("第3种拼接")
            return True

        # 第4种拼接情况
        cut = False
        right = True
        for i in range(size // 2):
            left, right = i, size - i - 1
            if not cut:
                if b[left] != a[right]:
                    if b[left] == b[right]:
                        cut = True
                    else:
                        right = False
                        break
            else:
                if b[left] != b[right]:
                    right = False
                    break
        if right:
            print("第4种拼接")
            return True

        return False
```