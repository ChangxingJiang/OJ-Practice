class Solution:
    def numberToWords(self, num: int) -> str:
        pass


if __name__ == "__main__":
    print(Solution().numberToWords(123))  # "One Hundred Twenty Three"
    print(Solution().numberToWords(12345))  # "Twelve Thousand Three Hundred Forty Five"
    print(Solution().numberToWords(1234567))  # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    print(Solution().numberToWords(
        1234567891))  # "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
