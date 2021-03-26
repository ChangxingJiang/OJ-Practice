class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        # ---------- 计算每个字母的出现频数 ----------
        lst1 = [0] * 26
        lst2 = [0] * 26
        for ch in a:
            lst1[ord(ch) - 97] += 1
        for ch in b:
            lst2[ord(ch) - 97] += 1

        s1, s2 = len(a), len(b)

        # ---------- 计算前缀和、后缀和 ----------
        prefix1 = [lst1[0]] + [0] * 25  # 当前位置左侧的a的数量
        prefix2 = [lst2[0]] + [0] * 25  # 当前位置左侧的a的数量
        suffix1 = [0] * 25 + [lst1[-1]]  # 当前位置右侧的a的数量
        suffix2 = [0] * 25 + [lst2[-1]]  # 当前位置右侧的b的数量
        for i in range(1, 26):
            prefix1[i] = prefix1[i - 1] + lst1[i]
            prefix2[i] = prefix2[i - 1] + lst2[i]
        for i in range(26 - 2, -1, -1):
            suffix1[i] = suffix1[i + 1] + lst1[i]
            suffix2[i] = suffix2[i + 1] + lst2[i]

        # ---------- 计算结果 ----------
        ans = s1 + s2
        for i in range(1, 26):
            # 第一种情况：a中每个字母严格小于b中的每个字母
            ans = min(ans, suffix1[i] + prefix2[i - 1])

            # 第二种情况：b中的每个字母严格小于a中的每个字母
            ans = min(ans, suffix2[i] + prefix1[i - 1])

        # 第三种情况：a和b都是同一个字母
        for i in range(26):
            ans = min(ans, s1 + s2 - lst1[i] - lst2[i])

        return ans


if __name__ == "__main__":
    print(Solution().minCharacters(a="aba", b="caa"))  # 2
    print(Solution().minCharacters(a="dabadd", b="cda"))  # 3
