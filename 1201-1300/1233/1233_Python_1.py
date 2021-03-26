from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # 将所有地址存入集合中
        folders = set(folder)

        # 遍历判断是否存在于集合中
        ans = []
        for f in folder:
            path = f.split("/")
            for i in range(1, len(path) - 1):
                if "/".join(path[:i + 1]) in folders:
                    break
            else:
                ans.append(f)

        return ans


if __name__ == "__main__":
    print(Solution().removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))  # ["/a","/c/d","/c/f"]
    print(Solution().removeSubfolders(folder=["/a", "/a/b/c", "/a/b/d"]))  # ["/a"]
    print(Solution().removeSubfolders(folder=["/a/b/c", "/a/b/d", "/a/b/ca"]))  # ["/a/b/c","/a/b/ca","/a/b/d"]
