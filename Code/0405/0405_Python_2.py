class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num = (pow(2, 32) - 1) - abs(num) + 1
        elif num == 0:
            return "0"
        ans = []
        while num > 0:
            d = str(num % 16)
            if d == "10":
                d = "a"
            elif d == "11":
                d = "b"
            elif d == "12":
                d = "c"
            elif d == "13":
                d = "d"
            elif d == "14":
                d = "e"
            elif d == "15":
                d = "f"
            ans.append(d)
            num //= 16
        ans.reverse()
        return "".join(ans)


if __name__ == "__main__":
    print(Solution().toHex(26))  # 1a
    print(Solution().toHex(-1))  # ffffffff
