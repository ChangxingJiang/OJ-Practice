# LeetCode题解(0068)：将单词数组转换为长度相等的文本行(Python)

题目：[原题链接](https://leetcode-cn.com/problems/text-justification/)（困难）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度             | 执行用时      |
| -------------- | ---------- | ---------------------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(L)$ : L为每行的长度 | 36ms (86.26%) |
| Ans 2 (Python) | $O(N)$     | $O(L)$ : L为每行的长度 | 36ms (86.26%) |
| Ans 3 (Python) |            |                        |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    idx = 0
    N = len(words)
    ans = []
    while idx < N:
        # 选择当前行的单词
        now = idx  # 当前坐标
        length = 0  # 当前选出词语长度总计
        while now < N and length + (now - idx - 1) <= maxWidth:
            length += len(words[now])
            now += 1

        # 处理非最后一行的情况
        if length + (now - idx - 1) > maxWidth:
            now -= 1
            length -= len(words[now])

            # 处理行中只有一个单词的情况
            if now - idx == 1:
                ans.append(words[idx] + " " * (maxWidth - length))

            # 处理行中有多个单词的情况
            else:
                # 计算额外需要补充的空格数量
                num, extra = divmod(maxWidth - length, now - idx - 1)  # num=每个间隔需添加的括号数，extra=额外需要添加的括号数

                # 生成当前行
                line = []
                for i in range(idx, now - 1):
                    line.append(words[i])
                    line.append(" " * num)
                    if i - idx < extra:
                        line.append(" ")
                line.append(words[now - 1])
                ans.append("".join(line))

        # 处理最后一行的情况
        else:
            ans.append(" ".join(words[idx:]) + " " * (maxWidth - length - (now - idx - 1)))

        idx = now

    return ans
```

解法二（整理解法一代码）：

```python
def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    idx = 0
    N = len(words)
    ans = []
    while idx < N:
        # 选择当前行的单词
        now = 0  # 当前单词数量
        length = 0  # 当前选出词语长度总计
        while idx + now < N and length + now - 1 <= maxWidth:
            length += len(words[idx + now])
            now += 1

        if length + now - 1 > maxWidth:  # 处理非最后一行的情况
            now -= 1
            length -= len(words[idx + now])

            if now == 1:  # 处理行中只有一个单词的情况
                ans.append(words[idx] + " " * (maxWidth - length))

            else:  # 处理行中有多个单词的情况
                num, extra = divmod(maxWidth - length, now - 1)  # num=每个间隔需添加的括号数，extra=额外需要添加的括号数

                line = []
                for i in range(now - 1):
                    line.append(words[idx + i])
                    line.append(" " * (num + (1 if i < extra else 0)))
                line.append(words[idx + now - 1])
                ans.append("".join(line))

        # 处理最后一行的情况
        else:
            ans.append(" ".join(words[idx:]) + " " * (maxWidth - length - (now - 1)))

        idx += now

    return ans
```