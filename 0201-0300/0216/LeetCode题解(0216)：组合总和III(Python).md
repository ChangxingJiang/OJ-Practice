# LeetCode题解(0216)：在1-9的数组中找到数量为A且和为B的所有组合(Python)

题目：[原题链接](https://leetcode-cn.com/problems/combination-sum-iii/)（中等）

标签：回溯算法、数组

| 解法           | 时间复杂度                     | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(S×K)$ : 其中S为最终答案数量 | $O(S×K)$   | 64ms (6.28%)  |
| Ans 2 (Python) | --                             | --         | 32ms (98.25%) |
| Ans 3 (Python) |                                |            |               |

解法一（递归）：

```python
class Solution:
    def __init__(self):
        self.ans = set()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def iterator(lst, total, num=1):
            # 处理当分支已经达到3个的情况
            if len(lst) == k:
                if total == n:
                    self.ans.add(tuple(lst))

            # 处理分支加上当前元素后小于目标值的情况
            if num <= 9 and total + num <= n:
                # 添加当前元素到分支
                iterator(lst + [num], total + num, num + 1)

                # 不添加当前元素到分支
                iterator(lst, total, num + 1)

        iterator([], 0)

        return [list(elem) for elem in self.ans]
```

解法二（使用itertools）：

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        for group in itertools.combinations([i for i in range(1, 10)], k):
            if sum(group) == n:
                ans.append(list(group))
        return ans
```