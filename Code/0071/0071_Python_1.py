class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        for p in path.split("/"):
            if p == ".." and ans:
                ans.pop()
            elif len(p) > 0 and p != "." and p != "..":
                ans.append(p)
        return "/" + "/".join(ans)


if __name__ == "__main__":
    print(Solution().simplifyPath("/home/"))  # "/home"
    print(Solution().simplifyPath("../../3-栈/"))  # "/"
    print(Solution().simplifyPath("/home//foo/"))  # "/home/foo"
    print(Solution().simplifyPath("/a/./b/../../c/"))  # "/c"
    print(Solution().simplifyPath("/a/../../b/../c//.//"))  # "/c"
    print(Solution().simplifyPath("/a//b////c/d//././/.."))  # ""/a/b/c"
