class Solution:
    def toHex(self, num: int) -> str:
        if num >= 0:
            return str(hex(num))[2:]
        else:
            return str(hex(int("FFFFFFFF", base=16) + num + 1))[2:]


if __name__ == "__main__":
    print(Solution().toHex(26))  # 1a
    print(Solution().toHex(-1))  # ffffffff
