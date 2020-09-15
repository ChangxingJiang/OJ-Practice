class Solution:
    def intToRoman(self, num: int) -> str:
        table = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                 (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

        ans = []
        for n, s in table:
            count, num = divmod(num, n)
            ans.append(count * s)

        return "".join(ans)


if __name__ == "__main__":
    print(Solution().intToRoman(3))  # "III"
    print(Solution().intToRoman(4))  # "IV"
    print(Solution().intToRoman(9))  # "IX"
    print(Solution().intToRoman(58))  # "LVIII"
    print(Solution().intToRoman(1994))  # "MCMXCIV"
