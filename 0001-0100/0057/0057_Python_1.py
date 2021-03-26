from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 计算当前新区间位置
        # 时间:O(N) 空间:O(N)
        left_new, right_new = newInterval
        left_interval, right_interval, inner_interval = [], [], set()  # 新区间的左右边缘所在的区间
        for left, right in intervals:
            # 包含新区间的左侧边缘
            if left <= left_new <= right:
                left_interval = [left, right]

            # 包含新区间的右侧边缘
            if left <= right_new <= right:
                right_interval = [left, right]

            # 被新区间包含
            if left_new <= left <= right <= right_new:
                inner_interval.add((left, right))

        # 处理新区间没有与老区间相交的情况
        # O(N)
        if not left_interval and not right_interval and not inner_interval:
            ans = []
            already_add = False
            for left, right in intervals:
                if not already_add and right_new < left:
                    already_add = True
                    ans.append([left_new, right_new])
                ans.append([left, right])
            if not already_add:
                ans.append([left_new, right_new])
            return ans

        # 处理新区间没有与老区间相交，但是被老区间包含的情况
        # O(N)
        if not left_interval and not right_interval and inner_interval:
            ans = []
            already_add = False
            for left, right in intervals:
                if (left, right) in inner_interval:
                    if not already_add:
                        already_add = True
                        ans.append([left_new, right_new])
                else:
                    ans.append([left, right])
            if not already_add:
                ans.append([left_new, right_new])
            return ans

        # 处理新区间被老区间包含的情况
        # O(1)
        if left_interval == right_interval:
            return intervals

        # 处理新区间与老区间相交的情况
        # O(N)
        ans = []
        for left, right in intervals:
            # 处理包含新区间的左侧边缘
            if [left, right] == left_interval:
                ans.append([left, right_new])

            # 处理包含新区间的右侧边缘
            elif [left, right] == right_interval:
                if ans and ans[-1][1] >= left_new:
                    ans[-1][1] = right
                else:
                    ans.append([left_new, right])

            # 处理被新区间包含
            elif (left, right) in inner_interval:
                if not ans or ans[-1][1] != right_new:
                    ans.append([left_new, right_new])

            else:
                ans.append([left, right])

        return ans


if __name__ == "__main__":
    # [[1,5],[6,9]]
    print(Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))

    # [[1,2],[3,10],[12,16]]
    print(Solution().insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))

    # [[5,7]]
    print(Solution().insert(intervals=[], newInterval=[5, 7]))

    # [[1,5],[6,8]]
    print(Solution().insert(intervals=[[1, 5]], newInterval=[6, 8]))

    # [[0,5]]
    print(Solution().insert(intervals=[[1, 5]], newInterval=[0, 3]))

    # [[0,5]]
    print(Solution().insert(intervals=[[1, 5]], newInterval=[0, 5]))

    # [[0,6]]
    print(Solution().insert(intervals=[[1, 5]], newInterval=[0, 6]))

    # [[0,9]]
    print(Solution().insert(intervals=[[1, 5], [6, 8]], newInterval=[0, 9]))

    # [[3,6],[9,9],[11,13],[14,14],[16,19],[20,22],[23,25],[29,34],[41,43],[45,49]]
    print(Solution().insert(
        intervals=[[3, 6], [9, 9], [11, 13], [14, 14], [16, 19], [20, 22], [23, 25], [30, 34], [41, 43], [45, 49]],
        newInterval=[29, 32])
    )
