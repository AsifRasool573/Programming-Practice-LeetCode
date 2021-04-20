35. Search Insert Position


Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Example 1: Input: nums = [1,3,5,6], target = 5 Output: 2

Example 2: Input: nums = [1,3,5,6], target = 2 Output: 1

Example 3: Input: nums = [1,3,5,6], target = 7 Output: 4

Example 4: Input: nums = [1,3,5,6], target = 0 Output: 0

Example 5: Input: nums = [1], target = 0 Output: 0




# First Logic (Working)

nums = [1,3,5,7,12,19,21]
target = 10
start = 0
end = len(nums)-1
while start <= end:
    
    mid = (start + end)//2
    if (nums[mid]==target):
        print(mid)
    elif (nums[mid]>target):
        end = mid-1
    else:
        start = mid+1
                
print(start)