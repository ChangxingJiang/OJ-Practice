class Solution:
    def intToRoman(self, num: int) -> str:
        B4 = ["", "M", "MM", "MMM"]
        B3 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        B2 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        B1 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return B4[num // 1000] + B3[num % 1000 // 100] + B2[num % 100 // 10] + B1[num % 10]


if __name__ == "__main__":
    print(Solution().intToRoman(3))  # "III"
    print(Solution().intToRoman(4))  # "IV"
    print(Solution().intToRoman(9))  # "IX"
    print(Solution().intToRoman(58))  # "LVIII"
    print(Solution().intToRoman(1994))  # "MCMXCIV"
