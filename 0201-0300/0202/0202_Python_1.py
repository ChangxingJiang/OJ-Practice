class Solution:
    def isHappy(self, n: int) -> bool:
        already = set()
        while n != 1:
            if n in already:
                return False
            already.add(n)
            n = sum([int(x) * int(x) for x in str(n)])
        return True


if __name__ == "__main__":
    print(Solution().isHappy(19))  # True
