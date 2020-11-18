from typing import List


class Solution:
    def __init__(self):
        self.reverse_lst = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }
        self.ans = []

    def findStrobogrammatic(self, n: int) -> List[str]:
        self.count(n, "")
        return self.ans

    def count(self, n: int, now: str, first: bool = True):
        if n == 0:
            self.ans.append(now)
        elif n <= len(now):
            self.count(n - 1, now + self.reverse_lst[now[n - 1]], first=False)
        elif n == 1 or n == len(now) + 1:
            for num in ["0", "1", "8"]:
                self.count(n - 1, now + num, first=False)
        else:
            if first:
                lst = ["1", "6", "8", "9"]
            else:
                lst = ["0", "1", "6", "8", "9"]
            for num in lst:
                self.count(n - 1, now + num, first=False)


if __name__ == "__main__":
    # ["0","1","8"]
    print(Solution().findStrobogrammatic(1))

    # ["11","69","88","96"]
    print(Solution().findStrobogrammatic(2))

    # ['101', '111', '181', '609', '619', '689', '808', '818', '888', '906', '916', '986']
    print(Solution().findStrobogrammatic(3))
