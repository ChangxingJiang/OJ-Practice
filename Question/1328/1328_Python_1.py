class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # 处理长度为1的特殊情况
        if len(palindrome) == 1:
            return ""

        # 检查是否可通过使字典序变小的替换完成替换
        mid = len(palindrome) // 2
        for i in range(mid):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i + 1:]

        # 将最后一个a替换为b
        return palindrome[:-1] + "b"


if __name__ == "__main__":
    print(Solution().breakPalindrome(palindrome="abccba"))  # "aaccba"
    print(Solution().breakPalindrome(palindrome="aa"))  # "ab"
    print(Solution().breakPalindrome(palindrome="a"))  # ""
    print(Solution().breakPalindrome(palindrome="aba"))  # "abb"
