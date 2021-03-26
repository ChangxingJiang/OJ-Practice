class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        if not S:
            return ""

        lst = []

        num = 0
        pos = 0
        for i, ch in enumerate(S):
            if ch == "1":
                num += 1
            else:
                num -= 1
            if num == 0:
                lst.append("1" + self.makeLargestSpecial(S[pos + 1:i]) + "0")
                pos = i + 1

        return "".join(sorted(lst, reverse=True))


if __name__ == "__main__":
    print(Solution().makeLargestSpecial(S="11011000"))  # "11100100"
    print(Solution().makeLargestSpecial(S="110110100100"))  # "111010010100"
    print(Solution().makeLargestSpecial(S="1010101100"))  # "1100101010"
    print(Solution().makeLargestSpecial(S="1011111100000010101100"))  # "1111110000001100101010"
    print(Solution().makeLargestSpecial(S="101110110011010000"))  # "111101001100100010"
    print(Solution().makeLargestSpecial(S="11101001111001010000110010"))  # "11111001010001101000110010"

