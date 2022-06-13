#Powers of 2

def powers_of_two(n):
    ans= []
    for i in range (0,n+1):
        temp=2**i
        ans.append(temp)
    return ans
