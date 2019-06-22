class SegmentTreeNode:
    def __init__(self, start, end, max_val):
        self.start = start
        self.end = end 
        self.max = max_val
        self.left = None
        self.right = None


class NumArray:
    def __init__(self, A):
        
        self.root = self.buildhelper(0, len(A) - 1, A)

    def buildhelper(self, left, right, A):
        if left > right:
            return None 

        root = SegmentTreeNode(left, right, A[left])

        if left == right:
            return root 

        mid = (left + right) // 2
        root.left = self.buildhelper(left, mid, A)
        root.right = self.buildhelper(mid+1, right, A)
        root.max = max(root.left.max, root.right.max)

        return root 

    def update(self, index, value):
        self._modify(self.root, index, value)
        

    def _modify(self, root, index, value):
        if root.start == root.end and root.start == index:
            root.max = value
            return

        mid = (root.start + root.end) // 2
        if index <= mid:
            self._modify(root.left, index, value)
            root.max = max(root.left.max, root.right.max)
        else:
            self._modify(root.right, index, value)
            root.max = max(root.left.max, root.right.max)
        return

    def rangeMaxQuery(self, start, end):
        return self._maxquery(self.root, start, end)
        
    def _maxquery(self, root, start, end):
        if start <= root.start and root.start <= end:
            return root.max
        mid = (root.start + root.end) // 2
        ans = -sys.maxsize
        if mid >= start:
            ans = max(ans, self._maxquery(root.left, start, end))
        if mid + 1 <= end:
            ans = max(ans, self._maxquery(root.right, start, end))
        return ans







