class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split("\n")

        ans = 0

        stack = []  # 当前路径栈
        for line in lines:
            num = line.count("\t")
            while len(stack) > num:
                stack.pop()
                
            name = line.replace("\t", "")

            # 处理当前为文件的情况
            if "." in line:
                ans = max(ans, sum(len(n) for n in stack) + len(stack) + len(name))
            else:
                stack.append(name)

        return ans


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
