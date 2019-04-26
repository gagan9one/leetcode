class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start=0
        l=len(matrix)
        end=l-1
        lim=l//2
        for j in range(0,lim):
            for i in range(start,end):
                matrix[i][j]+=matrix[l-1-j][i]
                matrix[l-1-j][i]=matrix[i][j]-matrix[l-1-j][i]
                matrix[i][j]-=matrix[l-1-j][i]
                
                matrix[l-1-j][i]+=matrix[l-1-i][l-1-j]
                matrix[l-1-i][l-1-j]=matrix[l-1-j][i]-matrix[l-1-i][l-1-j]
                matrix[l-1-j][i]-=matrix[l-1-i][l-1-j]
                
                matrix[l-1-i][l-1-j]+=matrix[j][l-1-i]
                matrix[j][l-1-i]=matrix[l-1-i][l-1-j]-matrix[j][l-1-i]
                matrix[l-1-i][l-1-j]-=matrix[j][l-1-i]
            start+=1
            end-=1
            print(matrix)