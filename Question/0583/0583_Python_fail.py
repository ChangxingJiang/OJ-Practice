class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1, N2 = len(word1), len(word2)
        if N1 == 0 and N2 == 0:
            return 0
        if N1 == 0 or N2 == 0:
            return N1 or N2

        queue_1, queue_2 = [], []

        i1, i2, ans = 0, 0, 0
        while i1 < N1 or i2 < N2:
            if i1 < N1 and i2 < N2 and word1[i1] == word2[i2]:
                ans += len(queue_1) + len(queue_2)
                queue_1, queue_2 = [], []
            elif i1 < N1 and word1[i1] in queue_2:
                tmp = queue_2.index(word1[i1])
                i2 = i2 - len(queue_2) + tmp
                ans += len(queue_1) + tmp
                queue_1, queue_2 = [], []
            elif i2 < N2 and word2[i2] in queue_1:
                tmp = queue_1.index(word2[i2])
                i1 = i1 - len(queue_2) + tmp
                ans += len(queue_2) + tmp
                queue_1, queue_2 = [], []
            else:
                if i1 < N1:
                    queue_1.append(word1[i1])
                if i2 < N2:
                    queue_2.append(word2[i2])
            if i1 < N1:
                i1 += 1
            if i2 < N2:
                i2 += 1
            # print(ans, i1, i2, N1, N2, word1[i1], word2[i2], queue_1, queue_2)
        # print(ans, queue_1, queue_2, i1, i2)
        return ans + len(queue_1) + len(queue_2)


if __name__ == "__main__":
    print(Solution().minDistance("sea", "eat"))  # 2
    print(Solution().minDistance("", ""))  # 0
    print(Solution().minDistance("se", ""))  # 2
    print(Solution().minDistance("a", "a"))  # 0
    print(Solution().minDistance("park", "spake"))  # 3
    print(Solution().minDistance("horse", "ros"))  # 4
    print(Solution().minDistance("dinitrophenylhydrazine", "dimethylhydrazine"))  # 9
