from typing import List


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        # 计算下一个字母的位置
        now = [-1] * 26
        table = [list(now)]
        for i in range(len(S) - 1, -1, -1):
            now[ord(S[i]) - 97] = i
            table.append(list(now))
        table.reverse()

        # 检查每个单词是否为子序列
        ans = 0
        for word in words:
            idx = 0
            for ch in word:
                if table[idx][ord(ch) - 97] == -1:
                    break
                else:
                    idx = table[idx][ord(ch) - 97] + 1
            else:
                ans += 1

        return ans


if __name__ == "__main__":
    # 3
    print(Solution().numMatchingSubseq(S="abcde", words=["a", "bb", "acd", "ace"]))
