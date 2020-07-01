# LeetCode题解(0744)：寻找比目标字母大的最小字母(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 136ms (69.15%) |
| Ans 2 (Python) | $O(logN)$  | $O(1)$     | 136ms (69.15%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（二分查找）：

```python
def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    if ord(letters[-1]) <= ord(target):
        return letters[0]
    left = 0
    right = len(letters) - 1
    while left < right:
        mid = (left + right) // 2
        if ord(letters[mid]) <= ord(target):
            left = mid + 1
        else:
            right = mid
    return letters[left]
```

解法二（二分查找）：

```python
def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    left = 0
    right = len(letters) - 1
    while left <= right:
        mid = (left + right) // 2
        if ord(letters[mid]) <= ord(target):
            left = mid + 1
        else:
            right = mid - 1
    if left == len(letters):
        return letters[0]
    else:
        return letters[left]
```