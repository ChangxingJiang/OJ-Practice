# LeetCode题解(Offer31)：判断两个序列是否可能为栈的压入和弹出序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/)（中等）

标签：栈、情景模拟

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (60.94%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 52ms (35.79%) |
| Ans 3 (Python) |            |            |               |

解法一（情景模拟1）：

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        N1 = len(pushed)
        N2 = len(popped)
        stack = []
        idx1 = 0
        idx2 = 0
        while idx1 < N1 or idx2 < N2:
            if stack and stack[-1] == popped[idx2]:
                stack.pop()
                idx2 += 1
            else:
                if idx1 < N1:
                    stack.append(pushed[idx1])
                    idx1 += 1
                else:
                    return False
        return not stack
```

解法二（情景模拟2）：

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        idx = 0
        for n in pushed:
            stack.append(n)
            while stack and stack[-1] == popped[idx]:
                stack.pop()
                idx += 1
        return not stack
```