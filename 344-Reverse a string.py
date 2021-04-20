344: Reverse a string

Problem Statement
Write a function that reverses a string. The input string is given as an array of characters s.

#First Logic

s = ["l","e","e","t","o"]
print('Original: ', s)

for i in range(len(s)):

  temp = s[i]

  s[i] = s[len(s)-(1+i)]

  s[len(s)-(1+i)] = temp

  if (i > len(s)-(1+i)):

    break;

print('Reversed:', s)



======================================================================================================
======================================================================================================



#second logic (Working)

s = ["p","a","k","i","s","t","a","n","1"]   
print(s)
start = 0
end = len(s)-1

while start < end:
  
  temp = s[start]
  s[start] = s[end]
  s[end] =temp
  start +=1
  end -=1

print(s)



======================================================================================================
======================================================================================================


#Third Logic (Working Pythonic)

s = ["p","a","k","i","s","t","a","n"]


for i in range(len(s)//2):
  s[i], s[-i-1] = s[-i-1], s[i]

