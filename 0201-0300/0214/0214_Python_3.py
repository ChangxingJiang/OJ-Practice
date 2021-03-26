class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s_new = s + "#" + s[::-1]
        N = len(s_new)

        table = [0] * N  # KMP失败函数
        length = 0  # 当前匹配字符串长度
        i = 1  # 当前坐标
        while i < N:
            if s_new[length] == s_new[i]:
                length += 1
                table[i] = length
                i += 1
            else:
                if length > 0:
                    length = table[length - 1]
                else:
                    i += 1
                    length = 0

        return s[table[-1]:][::-1] + s


if __name__ == "__main__":
    print(Solution().shortestPalindrome("aacecaaa"))  # "aaacecaaa"
    print(Solution().shortestPalindrome("abcd"))  # "dcbabcd"
    print(Solution().shortestPalindrome(""))  # ""
