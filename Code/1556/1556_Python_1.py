class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = []
        while True:
            if n >= 1000:
                a, b = divmod(n, 1000)
                ans.append(str(b).zfill(3))
                n = a
            else:
                ans.append(str(n))
                break
        return ".".join(ans[::-1])


if __name__ == "__main__":
    print(Solution().thousandSeparator(987))  # "987"
    print(Solution().thousandSeparator(1234))  # "1.234"
    print(Solution().thousandSeparator(123456789))  # "123.456.789"
    print(Solution().thousandSeparator(0))  # "0"
