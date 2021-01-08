class Solution:
    def minInteger(self, num: str, k: int) -> str:
        count = [[] for _ in range(10)]
        for i, ch in enumerate(num):
            count[int(ch)].append(i)
        print(count)


if __name__ == "__main__":
    print(Solution().minInteger(num="4321", k=4))  # "1342"
    print(Solution().minInteger(num="100", k=1))  # "010"
    print(Solution().minInteger(num="36789", k=1000))  # "36789"
    print(Solution().minInteger(num="22", k=22))  # "22"
    print(Solution().minInteger(num="9438957234785635408", k=23))  # "0345989723478563548"
