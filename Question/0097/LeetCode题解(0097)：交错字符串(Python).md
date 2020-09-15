# LeetCode题解(0097)：判断字符串是否由两字符串交错生成(Python)

题目：[原题链接](https://leetcode-cn.com/problems/interleaving-string/)（困难）

标签：字符串、动态规划

相关题目：与题目0072方法相似

| 解法           | 时间复杂度         | 空间复杂度               | 执行用时      |
| -------------- | ------------------ | ------------------------ | ------------- |
| Ans 1 (Python) | 最坏情况 : $O(MN)$ | 最坏情况 : $O(max(M,N))$ | 32ms (99.43%) |
| Ans 2 (Python) |                    |                          |               |
| Ans 3 (Python) |                    |                          |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（动态规划：用双端队列存储状态，用集合实现状态区中，减少无用的状态转移）：

![LeetCode题解(0097)：截图1](LeetCode题解(0097)：截图1.png)

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N1 = len(s1)
        N2 = len(s2)
        N3 = len(s3)
        visited = set()
        queue = collections.deque([(0, 0, 0)])  # 使用双向队列实现当前分支
        while queue:
            i1, i2, i3 = queue.popleft()
            if (i1, i2) not in visited:
                visited.add((i1, i2))
                if i3 == N3:
                    return i1 == N1 and i2 == N2
                if i1 < N1 and s1[i1] == s3[i3]:
                    queue.append((i1 + 1, i2, i3 + 1))
                if i2 < N2 and s2[i2] == s3[i3]:
                    queue.append((i1, i2 + 1, i3 + 1))
        return False
```