class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        s = list(str(N))

        i = 1
        while i < len(s) and int(s[i - 1]) <= int(s[i]):
            i += 1

        if i == len(s):
            return N

        while i > 0 and s[i - 1] > s[i]:
            s[i - 1] = str(int(s[i - 1]) - 1)
            i -= 1

        for i in range(i + 1, len(s)):
            s[i] = "9"

        return int("".join(s))


if __name__ == "__main__":
    print(Solution().monotoneIncreasingDigits(10))  # 9
    print(Solution().monotoneIncreasingDigits(1234))  # 1234
    print(Solution().monotoneIncreasingDigits(332))  # 299
