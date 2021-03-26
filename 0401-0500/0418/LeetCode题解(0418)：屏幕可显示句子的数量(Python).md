# LeetCode题解(0418)：屏幕可显示句子的数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sentence-screen-fitting/)（中等）

标签：动态规划、哈希表

| 解法           | 时间复杂度                       | 空间复杂度 | 执行用时       |
| -------------- | -------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×C)$                         | $O(S)$     | 超出时间限制   |
| Ans 2 (Python) | $O(C×T)$ : 其中T为循环节所用行数 | $O(S+T)$   | 268ms (70.00%) |
| Ans 3 (Python) |                                  |            |                |

解法一（完全暴力）：

```python
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentence = [len(word) for word in sentence]

        ans = 0
        i = 0

        count = {}

        info1 = 0
        info2 = 0

        for j in range(rows):
            length = cols
            while sentence[i] <= length:
                length -= sentence[i]
                i += 1
                if i == len(sentence):
                    ans += 1
                    i = 0

            # if i not in count:
            #     count[i] = (ans, j)

        return ans
```

解法二：

```python
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentence = [len(word) for word in sentence]

        ans = 0

        # 当前在sentence中的位置
        i = 0

        count = {}

        # 寻找循环
        idx = 0
        info1 = 0
        info2 = 0

        j = 0
        while j < rows:
            length = cols
            while sentence[i] <= length:
                length -= (sentence[i] + 1)
                i += 1
                if i == len(sentence):
                    ans += 1
                    i = 0

            j += 1

            if i not in count:
                count[i] = (ans, j)
            else:
                info1 = count[i]
                info2 = (ans, j)
                break

        # 如果在找到循环节之前已经完成遍历，则直接返回结果
        if j == rows:
            return ans

        n0 = info1[1] + 1  # 从no行开始重复
        n1 = info2[0] - info1[0]  # 每次循环重复n1次
        n2 = info2[1] - info1[1]  # 每次循环使用n1行

        # 移动循环节
        circle = (rows - n0 - n2) // n2
        ans += circle * n1
        j += circle * n2

        # 计算剩余部分
        while j < rows:
            length = cols
            while sentence[i] <= length:
                length -= (sentence[i] + 1)
                i += 1
                if i == len(sentence):
                    ans += 1
                    i = 0

            j += 1

        return ans
```