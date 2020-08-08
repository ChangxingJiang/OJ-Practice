class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        pass


if __name__ == "__main__":
    print(Solution().complexNumberMultiply("1+1i", "1+1i"))  # "0+2i"
    print(Solution().complexNumberMultiply("1+-1i", "1+-1i"))  # "0+-2i"
