# 时间:O(26×N^3×M) 空间:O(N)

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        def check(s1, s2):
            num = 0
            for ii in range(len(s1)):
                if s1[ii] != s2[ii]:
                    num += 1
                    if num >= 2:
                        return False
            return num == 1

        ans = 0
        for length in range(1, len(s) + 1):
            cache = {}
            for i in range(len(s) - length + 1):
                # 获取当前字符串
                pattern = s[i:i + length]

                # 如果没被计算过，则遍历t计算
                if pattern not in cache:
                    num = 0
                    for j in range(len(t) - length + 1):
                        if check(pattern, t[j:j + length]):
                            num += 1
                    cache[pattern] = num

                # 累加当前结果到答案
                # print(pattern, ":", cache[pattern])
                ans += cache[pattern]

        return ans


if __name__ == "__main__":
    print(Solution().countSubstrings(s="aba", t="baba"))  # 6
    print(Solution().countSubstrings(s="ab", t="bb"))  # 3
    print(Solution().countSubstrings(s="a", t="a"))  # 0
    print(Solution().countSubstrings(s="abe", t="bbc"))  # 10
