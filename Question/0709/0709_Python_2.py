class Solution:
    def toLowerCase(self, str: str) -> str:
        ans = ""
        for n in str:
            a = ord(n)
            if 65 <= ord(n) <= 90:
                ans += chr(a + 32)
            else:
                ans += n
        return ans


if __name__ == "__main__":
    print(Solution().toLowerCase("Hello"))  # hello
    print(Solution().toLowerCase("here"))  # here
    print(Solution().toLowerCase("LOVELY"))  # lovely
    print(Solution().toLowerCase("PiTAs"))  # lovely
