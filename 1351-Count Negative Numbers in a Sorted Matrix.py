1351. Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, 
return the number of negative numbers in grid.


Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.



#First Logic Working)

grid = [[4,3,2,-1],[3,2,-3,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
count = 0
for i in range(len(grid)):
  for j in range(len(grid[i])):
    if grid[i][j] < 0:
      count += 1

print(count)