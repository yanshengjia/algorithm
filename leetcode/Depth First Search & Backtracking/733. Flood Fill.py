"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.


Solution:
1.DFS recursion
首先判断如果给定位置的颜色跟新的颜色相同的话，直接返回，否则就对给定位置调用递归函数。在递归函数中，如果越界或者当前颜色跟起始颜色不同，直接返回。否则就给当前位置赋上新的颜色，然后对周围四个点继续调用递归函数。
2.BFS queue, like tree level order traversal
使用一个队列queue来辅助，首先将给定点放入队列中，然后进行while循环，条件是queue不为空，然后进行类似层序遍历的方法，取出队首元素，将其赋值为新的颜色，然后遍历周围四个点，如果不越界，且周围的颜色跟起始颜色相同的话，将位置加入队列中。
"""


# DFS with recursion
# Time Complexity: O(N), where NN is the number of pixels in the image. We might process every pixel.
# Space Complexity: O(N), the size of the implicit call stack when calling dfs.
class Solution:
    """
    @param image: a 2-D array
    @param sr: an integer
    @param sc: an integer
    @param newColor: an integer
    @return: the modified image
    """
    def floodFill(self, image, sr, sc, new_color):
        # Write your code here
        max_row, max_col, original_color = len(image), len(image[0]), image[sr][sc]
        self.dfs(image, sr, sc, original_color, new_color, max_row, max_col)
        return image
    
    def dfs(self, image, sr, sc, original_color, new_color, max_row, max_col):
        if 0 <= sr < max_row and 0 <= sc < max_col and image[sr][sc] != new_color and image[sr][sc] == original_color:
            image[sr][sc] = new_color    # update color
            for (i, j) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                self.dfs(image, sr + i, sc + j, original_color, new_color, max_row, max_col)


# BFS with queue
# Time Complexity: O(N), where NN is the number of pixels in the image. We might process every pixel.
# Space Complexity: O(N), the max size of the queue.
class Solution:
    """
    @param image: a 2-D array
    @param sr: an integer
    @param sc: an integer
    @param newColor: an integer
    @return: the modified image
    """
    def floodFill(self, image, sr, sc, new_color):
        # Write your code here
        max_row, max_col, original_color = len(image), len(image[0]), image[sr][sc]
        q = [(sr, sc)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while len(q) > 0:
            pixel = q.pop()
            # firstly check if the pixel in the range
            if 0 <= pixel[0] < max_row and 0 <= pixel[1] < max_col and image[pixel[0]][pixel[1]] == original_color and image[pixel[0]][pixel[1]] != new_color:
                image[pixel[0]][pixel[1]] = new_color
                neighbors = [(pixel[0]+direc[0], pixel[1]+direc[1]) for direc in directions]
                q.extend(neighbors)
        return image
    
