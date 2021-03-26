class Solution:
    def toHexspeak(self, num: str) -> str:
        res = hex(int(num))[2:].upper().replace("0", "O").replace("1", "I")
        return res if res.isalpha() else "ERROR"


if __name__ == "__main__":
    print(Solution().toHexspeak("257"))  # "IOI"
    print(Solution().toHexspeak("3"))  # "ERROR"
