class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        s1, s2 = len(sequence), len(word)

        ans = 0

        i1 = 0
        while i1 < s1:
            now, i2, i3 = 0, 0, i1
            while i3 < s1 and sequence[i3] == word[i2]:
                i2 += 1
                if i2 == s2:
                    now += 1
                    i2 = 0
                i3 += 1
            ans = max(ans, now)
            i1 += max(now - 1, 0) * s2 + 1

        return ans


if __name__ == "__main__":
    print(Solution().maxRepeating(sequence="ababc", word="ab"))  # 2
    print(Solution().maxRepeating(sequence="ababc", word="ba"))  # 1
    print(Solution().maxRepeating(sequence="ababc", word="ac"))  # 0
    print(Solution().maxRepeating(sequence="aaabaaaabaaabaaaabaaaabaaaabaaaaba", word="aaaba"))  # 5
