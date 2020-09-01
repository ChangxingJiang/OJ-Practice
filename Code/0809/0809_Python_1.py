from typing import List


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def change(s):
            exp = []
            for ch in s:
                if not exp or ch != exp[-1][0]:
                    exp.append([ch, 1])
                else:
                    exp[-1][1] += 1
            return exp

        S = change(S)
        N = len(S)

        ans = 0
        for word in words:
            word = change(word)
            if len(word) == N:
                for i in range(N):
                    if word[i][0] != S[i][0] or word[i][1] > S[i][1] or (word[i][1] == 1 and S[i][1] == 2):
                        break
                else:
                    ans += 1

        return ans


if __name__ == "__main__":
    print(Solution().expressiveWords(S="heeellooo", words=["hello", "hi", "helo"]))  # 1
