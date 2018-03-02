class Solution:
    def findMedianSortedArrays(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: float
        """
        if (len(A) == 0 or A is None) and (len(B) == 0 or B is None):
            return -1
        length = len(A) + len(B)
        if (length % 2 == 0):
            return (Solution.findKth(A, 0, B, 0, length // 2) + Solution.findKth(A, 0, B, 0, length // 2 + 1)) / 2;
        else:
            return Solution.findKth(A, 0, B, 0, length // 2 + 1)

    @staticmethod
    def findKth(A, idx_A, B, idx_B, k):
        if idx_A > (len(A) - 1):
            return B[idx_B + k - 1]
        if idx_B > (len(B) - 1):
            return A[idx_A + k - 1]
        if k == 1:
            return min(A[idx_A], B[idx_B])
        # try to get the median of A and B
        i = j = 2 ** 64
        if (idx_A + k // 2 - 1) < len(A):
            i = A[idx_A + k // 2 - 1]
        if (idx_B + k // 2 - 1) < len(B):
            j = B[idx_B + k // 2 - 1]

        if (i > j):
            return Solution.findKth(A, idx_A, B, idx_B + k // 2, k - k // 2)
        else:
            return Solution.findKth(A, idx_A + k // 2, B, idx_B, k - k // 2)