class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        N1, N2 = len(num1), len(num2)
        N = max(N1, N2) + 1
        now = 0
        ans = []
        for i in range(1, N + 1):
            now += int(num1[-i]) if i <= N1 else 0
            now += int(num2[-i]) if i <= N2 else 0
            now, n = divmod(now, 10)
            if i != N or now != 0 or n != 0:
                ans.append(str(n))
        return "".join(reversed(ans))


if __name__ == "__main__":
    print(Solution().addStrings("0", "0"))  # "0"
    print(Solution().addStrings("135", "2"))  # "137"
    print(Solution().addStrings("1", "9"))  # "10"
