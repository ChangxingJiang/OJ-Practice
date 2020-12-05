class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # R只能往左、L只能往右
        lst1, lst2 = [], []
        for i, ch in enumerate(start):
            if ch != "X":
                lst1.append((i, ch))
        for i, ch in enumerate(end):
            if ch != "X":
                lst2.append((i, ch))

        if len(lst1) != len(lst2):
            return False

        size = len(lst1)

        for i in range(size):
            i1, ch1 = lst1[i]
            i2, ch2 = lst2[i]
            if ch1 != ch2:
                return False
            if ch1 == "L" and i1 < i2:
                return False
            if ch1 == "R" and i1 > i2:
                return False

        return True


if __name__ == "__main__":
    # True
    print(Solution().canTransform(start="RXXLRXRXL",
                                  end="XRLXXRRLX"))
