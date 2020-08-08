from typing import List


class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        # 使用单调排序栈统计每一个元素奇偶跳的下一个元素
        size = len(A)
        next_odd = [-1] * size  # 奇跳的下一个元素(大于等于当前值的最小值)
        next_even = [-1] * size  # 偶跳的下一个元素(小于等于当前值的最大值)
        stack_odd = []  # 单调递减栈(用于计算奇跳)
        stack_even = []  # 单调递增栈(用于计算偶跳)
        for i in range(len(A) - 1, -1, -1):
            # 计算奇跳的下一个元素
            temp = []
            while stack_odd and A[stack_odd[-1]] < A[i]:
                temp.append(stack_odd.pop())
            if stack_odd:
                next_odd[i] = stack_odd[-1]
            if temp and A[temp[-1]] == A[i]:
                temp.pop()
            temp.append(i)
            while temp:
                stack_odd.append(temp.pop())

            # 计算偶跳的下一个元素
            temp = []
            while stack_even and A[stack_even[-1]] > A[i]:
                temp.append(stack_even.pop())
            if stack_even:
                next_even[i] = stack_even[-1]
            if temp and A[temp[-1]] == A[i]:
                temp.pop()
            temp.append(i)
            while temp:
                stack_even.append(temp.pop())

        print(next_odd, next_even)

        # 统计到达每一个元素的奇偶步数
        steps = [[1, 0] for _ in range(size)]  # 第1个为到达当前位置的该奇跳的数量，第2个为到达当前位置的该偶跳的数量
        for i in range(size):
            # 计算下一步为奇跳的情况
            if next_odd[i] != -1:
                steps[next_odd[i]][1] += steps[i][0]

            # 计算下一步为偶跳的情况
            if next_even[i] != -1:
                steps[next_even[i]][0] += steps[i][1]

        return steps[-1][0] + steps[-1][1]


if __name__ == "__main__":
    print(Solution().oddEvenJumps([10, 13, 12, 14, 15]))  # 2
    print(Solution().oddEvenJumps([2, 3, 1, 1, 4]))  # 3
    print(Solution().oddEvenJumps([5, 1, 3, 4, 2]))  # 3
