class Solution:
    def simplifyPath(self, path: str) -> str:
        pass


if __name__ == "__main__":
    print(Solution().simplifyPath("/home/"))  # "/home"
    print(Solution().simplifyPath("/../"))  # "/"
    print(Solution().simplifyPath("/home//foo/"))  # "/home/foo"
    print(Solution().simplifyPath("/a/./b/../../c/"))  # "/c"
    print(Solution().simplifyPath("/a/../../b/../c//.//"))  # "/c"
    print(Solution().simplifyPath("/a//b////c/d//././/.."))  # ""/a/b/c"
