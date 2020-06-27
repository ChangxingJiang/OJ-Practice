# LeetCode题解(0350)：求两个数组的交集(保留交集元素出现次数)(Python)

题目：[原题链接](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/)（简单）

| 解法           | 时间复杂度     | 空间复杂度  | 执行用时      |
| -------------- | -------------- | ----------- | ------------- |
| Ans 1 (Python) | O(n+m)         | O(n+m)      | 56ms (91.11%) |
| Ans 2 (Python) | O(n+m)         | O(min(n,m)) | 52ms (96.55%) |
| Ans 3 (Python) | O(nlogn+mlogm) | O(1)        | 56ms (91.11%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双哈希表）：

```python
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    hashmap1 = {}
    hashmap2 = {}
    for n in nums1:
        if n not in hashmap1:
            hashmap1[n] = 1
        else:
            hashmap1[n] += 1
    for n in nums2:
        if n in hashmap1:
            if n not in hashmap2:
                hashmap2[n] = 1
            else:
                hashmap2[n] += 1
    ans = []
    for n in hashmap1:
        if n in hashmap2:
            ans += [n] * min(hashmap1[n], hashmap2[n])
    return ans
```

解法二（单哈希表实现）：

```python
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    hashmap = {}

    # 选择较小的一个数组
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    # 将较小的一个数组存入哈希表
    for n in nums1:
        if n not in hashmap:
            hashmap[n] = 1
        else:
            hashmap[n] += 1

    ans = []
    for n in nums2:
        if n in hashmap and hashmap[n] > 0:
            ans.append(n)
            hashmap[n] -= 1
    return ans
```

解法三（排序）：

```python
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    index1 = 0
    index2 = 0
    ans = []
    while index1 <= len(nums1) - 1 and index2 <= len(nums2) - 1:
        if nums1[index1] < nums2[index2]:
            index1 += 1
        elif nums1[index1] > nums2[index2]:
            index2 += 1
        else:
            ans.append(nums1[index1])
            index1 += 1
            index2 += 1
    return ans
```