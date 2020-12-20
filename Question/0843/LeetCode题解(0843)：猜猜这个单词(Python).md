# LeetCode题解(0843)：猜猜这个单词(Python)

题目：[原题链接](https://leetcode-cn.com/problems/guess-the-word/)（困难）

标签：极小化极大

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (88.76%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        maybe_words = set(wordlist)

        for _ in range(10):
            guess = maybe_words.pop()
            result = master.guess(guess)
            if result == 6:
                return

            for word in list(maybe_words):
                same = sum(1 if word[i] == guess[i] else 0 for i in range(6))
                if same != result:
                    maybe_words.remove(word)
```