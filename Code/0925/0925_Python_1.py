class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        idx = 0
        for i in range(len(typed)):
            if idx < len(name) and typed[i] == name[idx]:
                idx += 1
            else:
                if i == 0 or typed[i] != name[idx - 1]:
                    return False
        return idx == len(name)


if __name__ == "__main__":
    print(Solution().isLongPressedName("alex", "aaleex"))  # True
    print(Solution().isLongPressedName("saeed", "ssaaedd"))  # False
    print(Solution().isLongPressedName("leelee", "lleeelee"))  # True
    print(Solution().isLongPressedName("laiden", "laiden"))  # True
    print(Solution().isLongPressedName("vtkgn", "vtkgnn"))  # True
