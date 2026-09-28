"""
LeetCode 54 · Spiral Matrix · Medium
https://leetcode.com/problems/spiral-matrix/

Pattern : Matrix / Simulation
Solved  : 28 Sep 2026
Time    : O(n) · Runtime: 0 ms (Beats 100.0%)
Space   : O(1) · Memory: 19.4 MB (Beats 35.6%)
"""

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        ans = []

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        while top <= bottom and left <= right:

            # Right
            for c in range(left, right + 1):
                ans.append(matrix[top][c])

            top += 1

            # Down
            for r in range(top, bottom + 1):
                ans.append(matrix[r][right])

            right -= 1

            # Left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    ans.append(matrix[bottom][c])

                bottom -= 1

            # Up
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    ans.append(matrix[r][left])

                left += 1

        return ans
