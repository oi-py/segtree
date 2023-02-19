#实现一个支持懒更新的线段树
#支持区间查询和区间修改
#区间修改：将区间内的所有元素加上一个值
#区间查询：查询区间内的最大值
#区间修改和区间查询的时间复杂度均为O(logn)
#懒更新：区间修改操作不会立即更新，而是在区间查询时才更新
#懒更新的时间复杂度为O(logn)
#懒更新的空间复杂度为O(n)
#使用数组实现
#数组下标从1开始
#数组下标为i的节点的左孩子下标为2*i
#数组下标为i的节点的右孩子下标为2*i+1
class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])
    
    def update(self, l, r, val):
        self._update(1, 0, self.n - 1, l, r, val)
    
    def query(self, l, r):
        return self._query(1, 0, self.n - 1, l, r)
    
    def _update(self, node, start, end, l, r, val):
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node]
            if start != end:
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0
        if start > end or start > r or end < l:
            return
        if start >= l and end <= r:
            self.tree[node] += val
            if start != end:
                self.lazy[2 * node] += val
                self.lazy[2 * node + 1] += val
        else:
            mid = (start + end) // 2
            self._update(2 * node, start, mid, l, r, val)
            self._update(2 * node + 1, mid + 1, end, l, r, val)
            self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def _query(self, node, start, end, l, r):
        if start > end or start > r or end < l:
            return -1
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node]
            if start != end:
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0
        if start >= l and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self._query(2 * node, start, mid, l, r)
        p2 = self._query(2 * node + 1, mid + 1, end, l, r)
        return max(p1, p2)
