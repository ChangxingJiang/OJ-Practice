class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 处理字符串长度过短的情况
        if len(s) < 2 ** k + 1:
            return False

        # 处理其他情况
        aim = 2 ** k
        lst = set()
        for i in range(len(s) - k + 1):
            lst.add(s[i:i + k])
            if len(lst) == aim:
                return True
        return False


if __name__ == "__main__":
    print(Solution().hasAllCodes(s="00110110", k=2))  # True
    print(Solution().hasAllCodes(s="00110", k=2))  # True
    print(Solution().hasAllCodes(s="0110", k=1))  # True
    print(Solution().hasAllCodes(s="0110", k=2))  # False
    print(Solution().hasAllCodes(s="0000000001011100", k=4))  # False
