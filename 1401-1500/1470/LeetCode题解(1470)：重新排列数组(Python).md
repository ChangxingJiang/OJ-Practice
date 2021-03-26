# LeetCode题解(1470)：重新排列数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shuffle-the-array/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 36ms (93.82%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 40ms (81.07%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def shuffle(self, nums: List[int], n: int) -> List[int]:
    ans1 = nums[:n]
    ans2 = nums[n:]
    ans = []
    for i in range(n):
        ans.append(ans1[i])
        ans.append(ans2[i])
    return ans
```

解法二：

```python
def shuffle(self, nums: List[int], n: int) -> List[int]:
    ans = []
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[n + i])
    return ans
```