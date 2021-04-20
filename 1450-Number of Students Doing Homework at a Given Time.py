1450. Number of Students Doing Homework at a Given Time

Problem Statement
Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

Return the number of students doing their homework at time queryTime. More formally,
return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.


Example 1:
Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1
Explanation: We have 3 students where:
The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.




#First Logic

startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4

count = 0

for i in range(len(startTime)):
  if endTime[i] >= queryTime:
    count +=1

print(count)


=============================================================

#2nd Logic

startTime = [9,8,7,6,5,4,3,2,1]
endTime = [10,10,10,10,10,10,10,10,10]
queryTime = 5

count = 0

for i in range(len(startTime)):
  if endTime[i] - startTime[i] >= queryTime:
    count +=1

print(count)


===============================================================

# 3rd Logic  (Working)
#now we'll try to make interval and check in it

startTime = [1,1,1,1]
endTime = [1,3,2,4]
queryTime = 3
count = 0

for i in range(len(startTime)):
  if queryTime in range(startTime[i], endTime[i]+1):      # *point
    count += 1

print(count)

# *point: we learnt that queryTime will always be >= startTime[i] and <= endTime[i]
# so we can build another logic

===========================================================================================


# 4th logic (this one also worked)

startTime = [9,8,7,6,5,4,3,2,1]
endTime = [10,10,10,10,10,10,10,10,10]
queryTime = 5
count = 0

for i in range(len(startTime)):
  if queryTime >= startTime[i] and queryTime <= endTime[i]:
    count+=1

print(count)