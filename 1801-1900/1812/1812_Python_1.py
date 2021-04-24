class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        lst1 = ["a", "c", "e", "g"]
        lst2 = ["1", "3", "5", "7"]
        ch1, ch2 = coordinates
        if not (ch1 in lst1 and ch2 in lst2) and (ch1 in lst1 or ch2 in lst2):
            return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().squareIsWhite("a1"))  # False
    print(Solution().squareIsWhite("h3"))  # True
    print(Solution().squareIsWhite("c7"))  # False
