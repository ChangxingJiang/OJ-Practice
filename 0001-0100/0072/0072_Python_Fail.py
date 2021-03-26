class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1, N2 = len(word1), len(word2)

        ans = 0

        i1 = i2 = 0  # 当前已确定对应的位置
        while i1 < N1 and i2 < N2:
            now = 0
            h1, h2 = {}, {}  # 记录之前查询信息
            r1, r2 = i1, i2  # 当前查询位置
            while r1 < N1 and r2 < N2:
                s1, s2 = word1[r1], word2[r2]  # 当前查询位置字符
                if s1 == s2:  # 处理当前查询的两个字符相同的情况
                    i1, i2 = r1 + 1, r2 + 1  # 移动当前已确定的位置
                    ans += now
                    break
                elif s1 in h2 and s2 not in h1:  # 处理s1已匹配的情况
                    i1 = r1 + 1  # 更新i1
                    i2 = h2[s1] + 1  # 更新i2
                    ans += now
                    break
                elif s2 in h1 and s1 not in h2:  # 处理s2已匹配的情况
                    i1 = h1[s2] + 1  # 更新i1
                    i2 = r2 + 1  # 更新i2
                    ans += now
                    break
                elif s1 in h2 and s2 in h1:  # 处理两侧同时匹配的情况：递归求解
                    return now + min(self.minDistance(word1[r1:], word2[h2[s1]:]), self.minDistance(word1[h1[s2]:], word2[r2:]))
                else:  # 处理两侧均没有匹配的情况
                    if r1 == N1 - 1 and r2 == N2 - 1:
                        r1 += 1
                        r2 += 1
                    else:
                        if r1 < N1 - 1:
                            h1[s1] = r1  # 记录当前查询信息
                            r1 += 1
                        if r2 < N2 - 1:
                            h2[s2] = r2  # 记录当前查询信息
                            r2 += 1
                now += 1
                # print("R:", r1, r2, "->", ans)
            if r1 == N1 or r2 == N2:
                break
            print("I:", i1, i2, "->", ans)

        # print("F:", i1, "/", N1, ";", i2, "/", N2)
        # print(word1, word2, "->", ans + max((N1 - i1), (N2 - i2)))

        return ans + max((N1 - i1), (N2 - i2))


if __name__ == "__main__":
    print(Solution().minDistance(word1="horse", word2="ros"))  # 3
    print(Solution().minDistance(word1="intention", word2="execution"))  # 5
    print(Solution().minDistance(word1="a", word2="b"))  # 1
    print(Solution().minDistance(word1="ab", word2="bc"))  # 2
    print(Solution().minDistance(word1="mart", word2="karma"))  # 3
    print(Solution().minDistance(word1="sea", word2="ate"))  # 3
    print(Solution().minDistance(word1="industry", word2="interest"))  # 3
