class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1.zfill(len(num2))
        num2 = num2.zfill(len(num1))
        carry = 0
        ans = []
        for i in range(1, len(num1) + 1):
            n1 = int(num1[-i])
            n2 = int(num2[-i])
            n = n1 + n2 + carry
            ans.append(str(n % 10))
            carry = n // 10
        if carry == 1:
            ans.append("1")
        ans.reverse()
        return "".join(ans)


if __name__ == "__main__":
    print(Solution().addStrings("0", "0"))  # "0"
    print(Solution().addStrings("135", "2"))  # "137"
    print(Solution().addStrings("1", "9"))  # "10"
