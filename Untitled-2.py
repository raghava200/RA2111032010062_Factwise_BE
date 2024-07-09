'''There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
 
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
 
Your score is the sum of the points of the cards you have taken.
 
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
 
Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
 
Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4
 
Example 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
'''
#CODE:
def max_score(card,k):
    n=len(card)
    total_points=sum(card)
    size=n-k
    min_window=float('inf')
    window_points=sum(card[:size])
    min_window=min(min_window,window_points)
    for i in range(size,n):
          window_points=window_points-card[i-size]+card[i]
          min_window=min(min_window,window_points)
    return total_points-min_window
input_list=list(map(int,input("enter the list:").split()))
k=int(input("K="))
print("result:",max_score(input_list,k))
