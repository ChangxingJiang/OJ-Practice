class Solution:
    def intToRoman(self, num: int) -> str:
        def translate(n, sign1, sign2, sign3):
            if n == 0:
                return ""
            elif 1 <= n <= 3:
                return sign1 * n
            elif n == 4:
                return sign1 + sign2
            elif 5 <= n <= 8:
                return sign2 + sign1 * (n - 5)
            elif n == 9:
                return sign1 + sign3

        a = translate(num // 1000, "M", "", "")
        b = translate(num % 1000 // 100, "C", "D", "M")
        c = translate(num % 100 // 10, "X", "L", "C")
        d = translate(num % 10, "I", "V", "X")
        return a + b + c + d


if __name__ == "__main__":
    print(Solution().intToRoman(3))  # "III"
    print(Solution().intToRoman(4))  # "IV"
    print(Solution().intToRoman(9))  # "IX"
    print(Solution().intToRoman(58))  # "LVIII"
    print(Solution().intToRoman(1994))  # "MCMXCIV"
