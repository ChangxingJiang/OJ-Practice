# LeetCode题解(1237)：找出给定方程的正整数解(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-positive-integer-solution-for-a-given-equation/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 64ms (54.59%) |
| Ans 2 (Python) | $O(logN)$  | $O(1)$     | 36ms (98.26%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双指针）：

```python
def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
    idx1 = 1
    idx2 = 1000
    ans = []
    while idx1 <= 1000 and idx2 >= 1:
        if customfunction.f(idx1, idx2) < z:
            idx1 += 1
        elif customfunction.f(idx1, idx2) > z:
            idx2 -= 1
        else:
            ans.append([idx1, idx2])
            idx1 += 1
            idx2 -= 1
    return ans
```

解法二（双指针+二分法）：

```python
def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
    idx1 = 1
    idx2 = 1000
    ans = []
    while idx1 <= 1000 and idx2 >= 1:
        if customfunction.f(idx1, idx2) < z:
            mid = (idx1 + idx2) // 2
            if customfunction.f(mid, idx2) < z:
                idx1 = max(mid, idx1 + 1)
            else:
                idx1 += 1
        elif customfunction.f(idx1, idx2) > z:
            mid = (idx1 + idx2) // 2
            if customfunction.f(idx1, mid) > z:
                idx2 = min(mid, idx2 - 1)
            else:
                idx2 -= 1
        else:
            ans.append([idx1, idx2])
            idx1 += 1
            idx2 -= 1
    return ans
```