# LeetCode题解(0040)：在不重复数组中找到和为目标数的所有组合(每个数字只能用一次)(Python)

题目：[原题链接](https://leetcode-cn.com/problems/combination-sum-ii/)（中等）

标签：回溯算法、数组

| 解法           | 时间复杂度                                                   | 空间复杂度     | 执行用时      |
| -------------- | ------------------------------------------------------------ | -------------- | ------------- |
| Ans 1 (Python) | $O(ClogC+N×L)$: 其中C为candidates的长度，N为最终答案数量，L为答案的平均长度 | $O(ClogC+N×L)$ | 44ms (94.19%) |
| Ans 2 (Python) |                                                              |                |               |
| Ans 3 (Python) |                                                              |                |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.ans = set()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def iterator(lst, total, idx=0):
            if idx >= len(candidates):
                return

            num = candidates[idx]

            # 处理分支加上当前元素后小于目标值的情况
            if total + num < target:
                # 添加当前元素到分支
                iterator(lst + [num], total + num, idx + 1)

                # 不添加当前元素到分支
                iterator(lst, total, idx + 1)

            elif total + num == target:
                lst.append(num)
                self.ans.add(tuple(lst))

        iterator([], 0)

        return [list(elem) for elem in self.ans]
```