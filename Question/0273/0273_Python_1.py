class Solution:
    def numberToWords(self, num: int) -> str:
        # 定义字典
        D1 = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
        D2 = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
              19: "Nineteen"}
        D3 = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}

        # 处理两位数以内的情况
        def get_0_99(n):
            if n == 0:
                return []
            elif n < 10:
                return [D1[n]]
            elif n < 20:
                return [D2[n]]
            else:
                a, b = divmod(n, 10)
                if b == 0:
                    return [D3[a]]
                else:
                    return [D3[a], D1[b]]

        # 处理三位数以内的情况
        def get_0_999(n):
            a, b = divmod(n, 100)
            if n < 100:
                return get_0_99(b)
            else:
                return [D1[a], "Hundred"] + get_0_99(b)

        # 处理万亿以内的情况
        ans = []
        if num >= 1000000000:
            now, num = divmod(num, 1000000000)
            ans += get_0_999(now) + ["Billion"]
        if num >= 1000000:
            now, num = divmod(num, 1000000)
            ans += get_0_999(now) + ["Million"]
        if num >= 1000:
            now, num = divmod(num, 1000)
            ans += get_0_999(now) + ["Thousand"]
        ans += get_0_999(num)
        return " ".join(ans) if ans else "Zero"


if __name__ == "__main__":
    print(Solution().numberToWords(0))  # "Zero"
    print(Solution().numberToWords(20))  # "Twenty"
    print(Solution().numberToWords(123))  # "One Hundred Twenty Three"
    print(Solution().numberToWords(12345))  # "Twelve Thousand Three Hundred Forty Five"
    print(Solution().numberToWords(1234567))  # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    print(Solution().numberToWords(
        1234567891))  # "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
