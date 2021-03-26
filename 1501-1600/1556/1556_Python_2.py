# O(logN)
# 数学

class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return "0"

        ans = []
        while n:
            n, num = divmod(n, 1000)
            ans.append(str(num).zfill(3) if n else str(num))

        return ".".join(ans[::-1])


if __name__ == "__main__":
    print(Solution().thousandSeparator(987))  # "987"
    print(Solution().thousandSeparator(1234))  # "1.234"
    print(Solution().thousandSeparator(123456789))  # "123.456.789"
    print(Solution().thousandSeparator(0))  # "0"
    print(Solution().thousandSeparator(51040))  # "51040"
