
                
                


def knapSack(W , weight , value , n): 
  
    if n == 0 or W == 0 : 
        return 0
  
 
    if (weight[n-1] > W): 
        return knapSack(W , weight , value , n-1) 
  

    else: 
        return max(value[n-1] + knapSack(W-weight[n-1] , weight , value , n-1), knapSack(W , weight , value , n-1)) 
  
 

value = [6, 10, 12, 14, 16] 
weight = [1, 2, 3, 4, 5] 
W = 50
n = len(value) 
print(knapSack(W , weight , value , n))




