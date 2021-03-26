from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = []
        last = " "
        folder.sort()
        for f in folder:
            if not f.startswith(last):
                ans.append(f)
                last = f + "/"
        return ans


if __name__ == "__main__":
    print(Solution().removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))  # ["/a","/c/d","/c/f"]
    print(Solution().removeSubfolders(folder=["/a", "/a/b/c", "/a/b/d"]))  # ["/a"]
    print(Solution().removeSubfolders(folder=["/a/b/c", "/a/b/d", "/a/b/ca"]))  # ["/a/b/c","/a/b/ca","/a/b/d"]
