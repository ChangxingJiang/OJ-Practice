import collections

class IntervalArray:
    class Interval:
        __slots__ = ("l", "r")

        def __init__(self, l, r):
            self.l = l
            self.r = r

        def __len__(self):
            return self.r - self.l + 1

        def __repr__(self):
            return str(str(self.l) + "-" + str(self.r))

    def __init__(self):
        self.mapping = collections.defaultdict(list)

    def add(self, x):
        # 处理当前数值不与任何序列相邻的情况
        if x not in self.mapping or len(self.mapping[x]) == 0:
            interval = self.Interval(x, x)
            self.mapping[x - 1].append(interval)
            self.mapping[x + 1].append(interval)

        # 处理当前数值只与一个序列相邻的情况
        elif len(self.mapping[x]) == 1:
            interval = self.mapping[x][0]
            del self.mapping[x]
            if x == interval.l - 1:
                interval.l -= 1
                self.mapping[x - 1].append(interval)
            else:
                interval.r += 1
                self.mapping[x + 1].append(interval)

        # 处理当前数值与两个序列相邻的情况
        else:
            interval1, interval2 = self.mapping[x][0], self.mapping[x][1]
            del self.mapping[x]
            if interval1.l > interval2.l:
                interval1, interval2 = interval2, interval1
            interval = self.Interval(interval1.l, interval2.r)
            self.mapping[interval1.l - 1].remove(interval1)
            self.mapping[interval2.r + 1].remove(interval2)
            self.mapping[interval1.l - 1].append(interval)
            self.mapping[interval2.r + 1].append(interval)