# LeetCode题解(1160)：判断可由指定字母拼写的所有单词总长(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters/)（简单）

| 解法           | 时间复杂度                                 | 空间复杂度              | 执行用时       |
| -------------- | ------------------------------------------ | ----------------------- | -------------- |
| Ans 1 (Python) | $O(N×K+C)$ : K为单词平均长度，C为chars长度 | $O(C)$ : C为chars的长度 | 400ms (9.72%)  |
| Ans 2 (Python) | $O(N×K+C)$ : K为单词平均长度，C为chars长度 | $O(C)$ : C为chars的长度 | 196ms (60.88%) |
| Ans 3 (Python) | $O(N×K+C)$ : K为单词平均长度，C为chars长度 | $O(C)$ : C为chars的长度 | 104ms (98.39%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（使用collections.Counter类）：

```python
def countCharacters(self, words: List[str], chars: str) -> int:
    pattern = collections.Counter(chars)
    ans = 0
    for word in words:
        count = pattern & collections.Counter(word)
        if len(list(count.elements())) == len(word):
            ans += len(word)
    return ans
```

解法二（哈希表计数）：

```python
def countCharacters(self, words: List[str], chars: str) -> int:
    pattern = collections.Counter(chars)
    ans = 0
    for word in words:
        count = pattern.copy()
        for c in word:
            if c not in count or count[c] <= 0:
                break
            else:
                count[c] -= 1
        else:
            ans += len(word)
    return ans
```

解法三（更好的哈希表计数）：

```python
def countCharacters(self, words: List[str], chars: str) -> int:
    pattern = collections.Counter(chars)
    ans = 0
    for word in words:
        for c in word:
            if c not in pattern or word.count1(c) > pattern[c]:
                break
        else:
            ans += len(word)
    return ans
```