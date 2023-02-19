class SegmentTreeNode:
    def __init__(self, l, r, val=0):
        self.l = l #左端点
        self.r = r #右端点
        self.val = val #节点值
        self.max = val #区间查询结果
        self.left = None #左子树
        self.right = None #右子树
    
    #创建左子树
    def create_left(self, val=0):
        self.left = SegmentTreeNode(self.l, (self.l + self.r) // 2, val)
    
    #创建右子树
    def create_right(self, val=0):
        self.right = SegmentTreeNode((self.l + self.r) // 2 + 1, self.r, val)

    #区间最大值查询
    #查询区间为[l, r]
    def queryMax(self, l, r):
        if l <= self.l and r >= self.r:
            return self.max
        if l > self.r or r < self.l:
            return -float('inf')
        if self.left is None:
            self.create_left(self.val)
        if self.right is None:
            self.create_right(self.val)
        return max(self.left.queryMax(l, r), self.right.queryMax(l, r))
    
    #区间修改
    #将区间[l, r]内的所有元素加上val
    def update(self, l, r, val):
        if l <= self.l and r >= self.r:
            self.val += val
            self.max += val
            return
        if l > self.r or r < self.l:
            return
        if self.left is None:
            self.create_left(self.val)
        if self.right is None:
            self.create_right(self.val)
        self.left.update(l, r, val)
        self.right.update(l, r, val)
        self.max = max(self.left.max, self.right.max)
