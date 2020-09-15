from typing import List


class Solution:
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


if __name__ == "__main__":
    # [
    #    "This    is    an",
    #    "example  of text",
    #    "justification.  "
    # ]
    print(Solution().fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16))

    # [
    #   "What   must   be",
    #   "acknowledgment  ",
    #   "shall be        "
    # ]
    print(Solution().fullJustify(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16))

    # [
    #   "Science  is  what we",
    #   "understand      well",
    #   "enough to explain to",
    #   "a  computer.  Art is",
    #   "everything  else  we",
    #   "do                  "
    # ]
    print(Solution().fullJustify(words=["Science", "is", "what", "we", "understand", "well", "enough", "to",
                                        "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], maxWidth=20))

    # [
    #   "ask   not   what",
    #   "your country can",
    #   "do  for  you ask",
    #   "what  you can do",
    #   "for your country"
    # ]
    print(Solution().fullJustify(
        words=["ask", "not", "what", "your", "country", "can", "do", "for", "you", "ask", "what", "you", "can", "do", "for", "your", "country"],
        maxWidth=16))
