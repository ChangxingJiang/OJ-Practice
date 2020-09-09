from toolkit import TreeNode


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        pass


if __name__ == "__main__":
    # [1,2,5,3,4,6,7]
    print(Solution().recoverFromPreorder("1-2--3--4-5--6--7"))

    # [1,2,5,3,null,6,null,4,null,7]
    print(Solution().recoverFromPreorder("1-2--3---4-5--6---7"))

    # [1,401,null,349,88,90]
    print(Solution().recoverFromPreorder("1-401--349---90--88"))
