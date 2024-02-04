class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # Start at top left [0,0] and go diagonally, then put the in acsending order
        # Then go to the [0,1] and do the same
        
        
        rows, columns = len(mat), len(mat[0])
        
        # Iterate over diagonals starting from the top row
        for i in range(rows):
            self.sortDiagonal(mat, i, 0)
        
        # Iterate over diagonals starting from the left column
        for j in range(1, columns):
            self.sortDiagonal(mat, 0, j)
            
        return mat
    
    
    def sortDiagonal(self, mat, rowIndex, columnIndex):
        """
            mat (List[List[int]]): Matrix we're sorting
            rowIndex (int): index of the current row
            columnIndex (int): index of the current column
        """
        
        diagonal = []
        
        while rowIndex < len(mat) and columnIndex < len(mat[0]):
            diagonal.append(mat[rowIndex][columnIndex])
            rowIndex += 1
            columnIndex += 1
            
        
        # Sort the diagonal
        
        diagonal.sort()
        
        # Add data back into the matrix
        
        rowIndex = rowIndex - len(diagonal)
        columnIndex = columnIndex - len(diagonal)
        
        for element in diagonal:
            mat[rowIndex][columnIndex] = element
            rowIndex += 1
            columnIndex +=1