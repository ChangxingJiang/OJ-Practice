class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)

        # 定义状态列表
        last1, last2 = 1, 1

        for i in range(1, len(s)):
            if s[i - 1] != "0" and int(s[i - 1:i + 1]) < 26:
                last1, last2 = last2, last1 + last2
            else:
                last1, last2 = last2, last2

        return last2


if __name__ == "__main__":
    print(Solution().translateNum(12258))  # 5
    print(Solution().translateNum(506))  # 1
