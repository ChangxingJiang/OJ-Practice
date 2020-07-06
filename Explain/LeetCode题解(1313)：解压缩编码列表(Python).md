# LeetCode题解(1313)：解压缩编码列表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/decompress-run-length-encoded-list/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (95.44%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def decompressRLElist(self, nums: List[int]) -> List[int]:
    ans = []
    for i in range(0, len(nums), 2):
        ans += [nums[i + 1]] * nums[i]
    return ans
```