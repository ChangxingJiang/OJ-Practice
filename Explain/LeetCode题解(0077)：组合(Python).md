# LeetCode题解(0077)：实现组合(itertools.combinations函数的功能)(Python)

题目：[原题链接](https://leetcode-cn.com/problems/combinations/)（中等）

标签：回溯算法、数学

| 解法           | 时间复杂度                                      | 空间复杂度 | 执行用时      |
| -------------- | ----------------------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | --                                              | --         | 40ms (99.20%) |
| Ans 2 (Python) | $O(N×K)$ : 其中N为组合结果数，K为每个组合的长度 | $O(K)$     | 56ms (89.15%) |
| Ans 3 (Python) |                                                 |            |               |

解法一（使用itertools实现）：

![LeetCode题解(0077)：截图](LeetCode题解(0077)：截图.png)

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(elem) for elem in itertools.combinations(range(1, n + 1), k)]
```

解法二：

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 下一个组合
        def change(group):
            for i in range(k):
                if group[k - 1 - i] < n - i:
                    group[k - 1 - i] += 1
                    for j in range(k - i, k):
                        group[j] = group[j - 1] + 1
                    return True
            return False

        ans = []
        now = [i for i in range(1, k + 1)]
        ans.append(now.copy())
        while change(now):
            ans.append(now.copy())

        return ans
```