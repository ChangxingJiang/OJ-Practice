class Solution:
    def confusingNumber(self, N: int) -> bool:
        s = str(N)

        lst = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6",
        }

        new = []
        for i in range(len(s)):
            if s[i] in ("2", "3", "4", "5", "7"):
                return False
            else:
                new.append(lst[s[i]])

        return s != "".join(new[::-1])


if __name__ == "__main__":
    print(Solution().confusingNumber(6))  # True
    print(Solution().confusingNumber(89))  # True
    print(Solution().confusingNumber(11))  # False
    print(Solution().confusingNumber(25))  # False
    print(Solution().confusingNumber(916))  # False
