from collections import deque 
class Solution:

    def matrixDFS(self,image: List[List[int]], sr: int, sc: int, color: int, starting_color: int) -> list[list[int]]:
        if sr < 0 or sc < 0 or sr == len(image) or sc == len(image[0]) or  (image[sr][sc] != starting_color):
            return image
            
        image[sr][sc] = color

        image = self.matrixDFS(image, sr+1, sc, color, starting_color)
        image = self.matrixDFS(image, sr-1, sc, color, starting_color)
        image = self.matrixDFS(image, sr, sc+1, color, starting_color)
        image = self.matrixDFS(image, sr, sc-1, color, starting_color)
        return image

# """ visit = [] #reflect: do I need this? or can I just colour as  Igot and if vertex == color we know its visited? I think this runs into the issue of collectings its neighbours - we no longer have their starting color - nevermind, this is only essentail for path-collection - I dont care which path or step colours a node"""
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

       
        starting_color = image[sr][sc]
        if starting_color == color:
            return image

        return self.matrixDFS(image, sr,sc,color, starting_color)


        

            







        

    #color - target colour post filling

    #check min and max bound, check if visited, check if wall

    #check if goal? or if left in queue? (i.e., all possible reached)

    # keep a count +=... if relevant

        #unvisit the node once all paths go through it means no more paths from current node exist, so we dont have to worry about double counting, but we are worried about the node being visited by a different path starting in a different node that did not visit it yet