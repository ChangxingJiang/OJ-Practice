class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ","%20")


if __name__ == "__main__":
    # "We%20are%20happy."
    print(Solution().replaceSpace("We are happy."))
