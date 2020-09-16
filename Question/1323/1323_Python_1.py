class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num)
        if "6" not in s:
            return num
        else:
            i = s.index("6")
            return num + 3 * (10 ** (len(s) - i - 1))


if __name__ == "__main__":
    print(Solution().maximum69Number(9669))  # 9969
    print(Solution().maximum69Number(9996))  # 9999
    print(Solution().maximum69Number(9999))  # 9999
