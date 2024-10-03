# https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,arr1,arr2):
        #code here
        answer = set(arr1) | set(arr2)
        
        return len(answer)

