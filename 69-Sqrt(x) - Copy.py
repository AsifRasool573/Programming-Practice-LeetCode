69. Sqrt(x)
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4 Output: 2

Example 2:

Input: 8 Output: 2

Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.




#First Logic (Working) (Binary search)

x = 8

if x<2:
    print(x)

start = 1
end = x//2

while start <= end:
    mid = (start + end)//2
    temp = mid * mid
    if temp == x:
        print(mid)
        break
        
    elif temp > x:
        end = mid -1
        
    else:
        start = mid+1

print(start-1)