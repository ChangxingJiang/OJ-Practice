# LeetCode题解(1170)：比较字符串最小字母的出现频次(Python)

题目：[原题链接](https://leetcode-cn.com/problems/compare-strings-by-frequency-of-the-smallest-character/)（简单）

| 解法           | 时间复杂度                 | 空间复杂度              | 执行用时       |
| -------------- | -------------------------- | ----------------------- | -------------- |
| Ans 1 (Python) | $O(N×M)$ : M为words的长度  | $O(M)$ : M为words的长度 | 508ms (46.91%) |
| Ans 2 (Python) | $O(N×M)$ : M为words的长度  | $O(M)$ : M为words的长度 | 480ms (61.80%) |
| Ans 3 (Python) | $O(NlogM)$: M为words的长度 | $O(M)$: M为words的长度  | 72ms (99.16%)  |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表）：

```python
def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
    word_num = []
    for word in words:
        count = collections.Counter(word)
        word_num.append(count[sorted(count.keys())[0]])

    ans = []
    for query in queries:
        count = collections.Counter(query)
        num = count[sorted(count.keys())[0]]
        k = 0
        for w in word_num:
            if w > num:
                k += 1
        ans.append(k)

    return ans
```

解法二（优化解法一的最小值出现频次计算方法）：

```python
def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
    word_num = []
    for word in words:
        word_num.append(word.count(min(word)))

    ans = []
    for query in queries:
        num = query.count(min(query))
        k = 0
        for w in word_num:
            if w > num:
                k += 1
        ans.append(k)

    return ans
```

解法三（优化解法二中的查找方法）：

```python
def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
    words = [word.count(min(word)) for word in words]
    words.sort()

    ans = []
    for query in queries:
        num = query.count(min(query))
        count = len(words) - bisect.bisect_right(words, num)
        ans.append(count)

    return ans
```

