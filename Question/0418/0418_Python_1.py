from typing import List


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


if __name__ == "__main__":
    # 1
    print(Solution().wordsTyping(rows=2, cols=8, sentence=["hello", "world"]))

    # 2
    print(Solution().wordsTyping(rows=3, cols=6, sentence=["a", "bcd", "e"]))

    # 1
    print(Solution().wordsTyping(rows=4, cols=5, sentence=["I", "had", "apple", "pie"]))

    # 50000000
    print(Solution().wordsTyping(rows=10000, cols=10000, sentence=["a"]))
