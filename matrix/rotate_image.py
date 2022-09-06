class Solution:

    def print_matrix(self, matrix):
        for row in matrix:
            print(str(row))
        print("")


    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        Solution().print_matrix(matrix)
        l, r = 0, len(matrix) - 1       # matrix is square so len(matrix) can be used instead of len(matrix[0]) for just the columns

        while l < r:
            for i in range(r - l):      # iterate through whole row except last element: (l, r-1) OR (r - l)
                top, bottom = l, r      # square matrix so top/bottom is same as l/r

                # save the topleft
                topLeft = matrix[top][l + i]

                # move bottom left in top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft

            r -= 1
            l += 1

        Solution().print_matrix(matrix)


test_matrix = [[1,2,3],[4,5,6],[7,8,9]]
test_matrix_2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

Solution().rotate(test_matrix)
Solution().rotate(test_matrix_2)

