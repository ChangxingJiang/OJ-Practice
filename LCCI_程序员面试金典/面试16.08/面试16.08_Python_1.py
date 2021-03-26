class Solution:
    # 处理[0,20)的情况
    def count1(self, n):
        return ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                "Nineteen"][n]

    # 处理[20,100)的情况
    def count2(self, n):
        a, b = divmod(n, 10)
        ans = [["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"][a - 2]]
        if b:
            ans.append(self.count1(b))
        return " ".join(ans)

    # 处理[0,100)的情况
    def count3(self, n):
        if n < 20:
            return self.count1(n)
        else:
            return self.count2(n)

    # 处理[100,1000)的情况
    def count4(self, n):
        a, b = divmod(n, 100)
        ans = [self.count1(a), "Hundred"]
        if b:
            ans.append(self.count3(b))
        return " ".join(ans)

    # 处理[0,1000)的情况
    def count5(self, n):
        if n < 100:
            return self.count3(n)
        else:
            return self.count4(n)

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ans = []
        name = ["Billion", "Million", "Thousand", None]
        while num > 0:
            num, now = divmod(num, 1000)
            b = name.pop()
            if b and now:
                ans.append(b)
            if now:
                ans.append(self.count5(now))

        return " ".join(ans[::-1])


if __name__ == "__main__":
    print(Solution().numberToWords(123))  # "One Hundred Twenty Three"
    print(Solution().numberToWords(1000))  # "One Thousand"
    print(Solution().numberToWords(12345))  # "Twelve Thousand Three Hundred Forty Five"
    print(Solution().numberToWords(1234567))  # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    print(Solution().numberToWords(
        1234567891))  # "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
