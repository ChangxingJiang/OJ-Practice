# LeetCode题解(1122)：数组的相对排序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/relative-sort-array/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 40ms (98.29%) |
| Ans 2 (Python) | $O(N+M)$   | $O(M)$     | 44ms (92.79%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（自定义排序）：

```python
def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    def helper(key):
        if key in arr2:
            return 0, arr2.index(key)
        else:
            return 1, key

    arr1.sort(key=helper)

    return arr1
```

解法二：

```python
def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    count = collections.Counter(arr1)
    ans = []
    for n in arr2:
        if n in count:
            for _ in range(count[n]):
                ans.append(n)
            del count[n]
    ans += sorted(list(count.elements()))
    return ans
```