class Solution:
    def findContestMatch(self, n: int) -> str:
        return self.recursion([str(i) for i in range(1, n + 1)])

    def recursion(self, lst):
        size = len(lst)
        if size == 1:
            return lst[0]
        else:
            return self.recursion(["(" + lst[i] + "," + lst[size - i - 1] + ")" for i in range(size // 2)])


if __name__ == "__main__":
    print(Solution().findContestMatch(2))  # (1,2)
    print(Solution().findContestMatch(4))  # ((1,4),(2,3))
    print(Solution().findContestMatch(8))  # (((1,8),(4,5)),((2,7),(3,6)))
