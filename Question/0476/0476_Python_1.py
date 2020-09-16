class Solution:
    def findComplement(self, num: int) -> int:
        return int(bin(num).replace("0b", "").replace("0", "2").replace("1", "0").replace("2", "1"), base=2)


if __name__ == "__main__":
    print(Solution().findComplement(5))  # 2
    print(Solution().findComplement(1))  # 0
