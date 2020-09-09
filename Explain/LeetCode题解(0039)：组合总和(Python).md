# LeetCode题解(0039)：在不重复数组中找到和为目标数的所有组合(Python)

题目：[原题链接](https://leetcode-cn.com/problems/combination-sum/)（中等）

标签：回溯算法、数组

| 解法           | 时间复杂度                                                   | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------------------------------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(ClogC+N×L)$ : 其中C为candidates的长度，N为最终答案数量，L为答案的平均长度 | $O(C+N×L)$ | 52ms (91.60%) |
| Ans 2 (Python) |                                                              |            |               |
| Ans 3 (Python) |                                                              |            |               |

解法一：

```python
    def __init__(self):
        self.ans = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def iterator(lst, total, idx=0):
            num = candidates[idx]

            # 处理当前分支仍小于目标值的情况
            if total + num < target:
                # 进入添加当前值的分支
                iterator(lst + [num], total + num, idx)

                # 进入不添加当前值的分支
                if idx + 1 < len(candidates):
                    iterator(lst, total, idx + 1)

            # 处理当前分支等于目标值的情况
            elif total + num == target:
                lst.append(num)
                self.ans.append(lst.copy())

        iterator(lst=[], total=0)

        return self.ans

```