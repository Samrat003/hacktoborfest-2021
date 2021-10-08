#code to find kth number which is not divisible by n
def kth_no_not_divisible(n,k):
    low = 1
    high = 999999999
    x = 0
    while (low <= high):
        mid = low+(high-low)/2
        result = mid - mid / n
        if (result > k):
            high = mid - 1
            
        elif (result < k):
            low = mid + 1
            
        else:
            x = mid
            high = mid - 1

    return x
    
n=int(input("enter value of n: "))
k=int(input("enter value of k: "))
print("\n\nkth number is: ",kth_no_not_divisible(n, k))
