# LeetCode题解(0966)：多条件的元音拼写检查器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/vowel-spellchecker/)（中等）

标签：字符串、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(M+N)$   | $O(M)$     | 240ms (52.17%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # 处理wordlist列表
        word_set = set(wordlist)  # 用于匹配区分大小写的结果

        word_dict = collections.defaultdict(list)  # 用于匹配大小写问题的单词
        vowel_dict = collections.defaultdict(list)  # 用于匹配元音问题的单词
        for word in wordlist:
            lower = word.lower()
            word_dict[lower].append(word)
            vowel_dict[re.sub("[aeiou]", "#", lower)].append(word)

        # 执行匹配
        ans = []
        for query in queries:
            if query in word_set:
                ans.append(query)
            else:
                lower = query.lower()
                if lower in word_dict:
                    ans.append(word_dict[lower][0])
                else:
                    vowel = re.sub("[aeiou]", "#", lower)
                    if vowel in vowel_dict:
                        ans.append(vowel_dict[vowel][0])
                    else:
                        ans.append("")

        return ans
```