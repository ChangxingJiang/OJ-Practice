class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # 处理特殊情况
        if n == "1":
            return "0"

        # 计算字符串中分隔位置的坐标
        idx_1 = (len(n) + 1) // 2  # 包含中间位置的坐标
        idx_2 = len(n) // 2  # 不包含中间位置的坐标

        ans = []

        # 计算第一种可能的答案（直接翻转后半部分）
        if n != n[::-1]:
            ans.append(int(n[:idx_1] + n[:idx_2][::-1]))

        # 计算第二种可能的答案（前半部分加1后翻转后半部分）
        temp = str(int(n[:idx_1]) + 1)
        ans.append(int(temp + temp[:idx_2][::-1]))

        # 计算第三种可能的答案（前半部分减1后翻转后半部分）
        if n == "1" + "0" * (len(n) - 1) or n == "1" + "0" * (len(n) - 2) + "1":  # 处理10、100等特殊情况
            ans.append(int("9" * (len(n) - 1)))
        else:
            temp = str(int(n[:idx_1]) - 1)
            ans.append(int(temp + temp[:idx_2][::-1]))

        # 选择其中差值最小的答案
        n = int(n)
        return str(sorted(ans, key=lambda i: (abs(i - n), i))[0])


if __name__ == "__main__":
    print(Solution().nearestPalindromic("123"))  # "121"
    print(Solution().nearestPalindromic("1234"))  # "1221"
    print(Solution().nearestPalindromic("1000"))  # "999"
    print(Solution().nearestPalindromic("999"))  # "1001"
    print(Solution().nearestPalindromic("10"))  # "9"
    print(Solution().nearestPalindromic("1"))  # "0"
    print(Solution().nearestPalindromic("11"))  # "9"
    print(Solution().nearestPalindromic("8"))  # "7"
