class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1, s2 = len(word1), len(word2)

        ans = []

        i1, i2 = 0, 0
        while i1 < s1 and i2 < s2:
            ans.append(word1[i1] + word2[i2])
            i1 += 1
            i2 += 1

        if i1 < s1:
            ans.append(word1[i1:])
        if i2 < s2:
            ans.append(word2[i2:])

        return "".join(ans)


if __name__ == "__main__":
    print(Solution().mergeAlternately(word1="abc", word2="pqr"))  # apbqcr
    print(Solution().mergeAlternately(word1="ab", word2="pqrs"))  # apbqrs
    print(Solution().mergeAlternately(word1="abcd", word2="pq"))  # apbqcd
