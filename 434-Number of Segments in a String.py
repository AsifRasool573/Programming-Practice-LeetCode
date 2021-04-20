434. Number of Segments in a String


You are given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.

# first logic // somehow works

s = "love live! mu'sic forever"

count = 0
if s == '':
  print(count)
for i in s:
  if i == ' ':
    count +=1

print(count+1)

========================================================================

# Second Logic(Working)

s = "love live! mu'sic forever"
count = 0
for i in range(len(s)):
  if s[i] != " " and (i==0 or s[i-1]== " "):
    count+=1

print(count)


========================================================================

# 3rd Logic with the help of Split. its working too

s = "                 hello     "
count = 0
for i in s.split(" "):
  if i!="":
    count+=1

print(count)