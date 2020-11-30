class Solution:
    def lengthLongestPath(self, input: str) -> int:
        pass


if __name__ == "__main__":
    # 20
    print(Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))

    # 32
    print(Solution().lengthLongestPath(
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))

    # 0
    print(Solution().lengthLongestPath("a"))

    # 12
    print(Solution().lengthLongestPath("file1.txt\nfile2.txt\nlongfile.txt"))
