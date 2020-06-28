# LeetCode精讲(0350)：求两个数组的交集(保留交集元素出现次数)(Python)

## 题目内容

给定两个数组，编写一个函数来计算它们的交集。

**示例 1：**

```
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
```

**示例 2：**

```
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
```

**说明：**

* 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
* 我们可以不考虑输出结果的顺序。

**进阶：**

* 如果给定的数组已经排好序呢？你将如何优化你的算法？
* 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
* 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii

## 解法效率

| 解法           | 时间复杂度     | 空间复杂度  | 执行用时      |
| -------------- | -------------- | ----------- | ------------- |
| Ans 1 (Python) | O(n+m)         | O(n+m)      | 56ms (91.11%) |
| Ans 2 (Python) | O(n+m)         | O(min(n,m)) | 52ms (96.55%) |
| Ans 3 (Python) | O(nlogn+mlogm) | O(1)        | 56ms (91.11%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

### 解法一（双哈希表）：

> **【思路】**
>
> 最直接的，我们会想到使用两个哈希表，分别存储两个数组的值；而后再通过比较两个哈希表中的值来判断两个数组的交集。

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

### 解法二（单哈希表实现）：

> **【思路】**
>
> 在解法一种，实际上我们不但对两个数组分别进行了遍历，而且还对其中一个映射的哈希表进行了遍历，时间复杂度较高；另外，我们分别存储了两个数组的映射哈希表，空间复杂度也较高。但是，实际上我们在遍历第二个数组的时候，就已经可以通过和第一个数组的哈希表进行比较得出结果了。
>
> 在实际操作中，我们在遍历第二个数组时，如果发现当前数存在于哈希表中，则可将该数添加到答案中，并在哈希表中减去该数，这样我们就可以仅对两个数组各进行一次遍历就得到结果了。
>
> 在生成映射哈希表的选择时，我们应选择相对较小的数组，这样占用的空间复杂度更小。

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

### 解法三（排序）：

> **【思路】**
>
> 除以上解法外，我们还可以先将两个数组排序，并分别使用一个指针进行遍历来判断交集。但是，这个方法相较于以上的解法，除需要对两个数组遍历外，还需要对两个数组进行排序，因此时间复杂度更高。

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