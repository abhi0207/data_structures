# Python function to print common elements in three sorted arrays
def findCommon(ar1, ar2, ar3, n1, n2, n3):
     
    # Initialize starting indexes for ar1[], ar2[] and ar3[]
    i, j, k = 0, 0, 0
     
    # Iterate through three arrays while all arrays have elements    
    while (i < n1 and j < n2 and k< n3):
         
        # If x = y and y = z, print any of them and move ahead 
        # in all arrays
        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
            print ar1[i],
            i += 1
            j += 1
            k += 1
         
        # x < y    
        elif ar1[i] < ar2[j]:
            i += 1
             
        # y < z    
        elif ar2[j] < ar3[k]:
            j += 1
         
        # We reach here when x > y and z < y, i.e., z is smallest    
        else:
            k += 1
