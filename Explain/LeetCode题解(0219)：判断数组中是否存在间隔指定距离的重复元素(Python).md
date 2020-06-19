# LeetCode题解(0219)：判断数组中是否存在间隔指定距离的重复元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/contains-duplicate-ii/)（简单）——本题题目描述存在不清晰之处

| 解法           | 时间复杂度 | 空间复杂度  | 执行用时      |
| -------------- | ---------- | ----------- | ------------- |
| Ans 1 (Python) | O(n)       | O(n)        | 48ms (>75.9%) |
| Ans 2 (Python) | $O(n^2)$   | O(min(n,k)) | 超出时间限制  |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（使用哈希表存储）：

```python
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    hashmap = {}
    for i in range(len(nums)):
        n = nums[i]
        if n not in hashmap or i-hashmap[n]>k:
            hashmap[n] = i
        else:
            return True
    else:
        return False
```

解法二（使用List维护窗口）：

```python
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    hashset = []
    for i in range(len(nums)):
        n = nums[i]
        if n not in hashset:
            hashset.append(n)
            if len(hashset) > k:
                hashset.pop(0)
        else:
            return True
    else:
        return False
```