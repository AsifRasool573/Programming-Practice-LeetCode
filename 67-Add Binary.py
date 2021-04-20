67. Add Binary
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1: Input: a = "11", b = "1" Output: "100"

Example 2: Input: a = "1010", b = "1011" Output: "10101"




#First Logic (Working)

#1st Approach
# 1. str binary to int binary
# 2. binary to decimal a=10, b= 11
# 3. decimal addition 10+11
# 4. decimal to str(binary) 21 => binary => string

a = "1010"
b = "1011"
adecimal,i=0,0
a=int(a)
# creating second number to decimal
while (a !=0 ):
    dec = a %10;
    adecimal += dec * pow(2,i)
    a = a // 10
    i+=1
# print(adecimal)


#printig 2nd number to decimal
b=int(b)
bdecimal=0
i=0
while (b !=0 ):
    dec = b % 10;
    bdecimal += dec * pow(2,i)
    b = b // 10
    i+=1
# print(bdecimal)

#adding decimals
sum = adecimal + bdecimal
# print(sum)

#decimal to binary
sumbinary = bin(sum).replace("0b","")
# print(str(sumbinary))
return str(sumbinary)


=============================================================

#2nd Logic (Working)
# #2nd Approach
# 1. make both of same length
# 2. add each character
#     2.1. dealing with carry
# 4. if any leftover carry

a = "11"
b = "1"

alen= len(a)
blen= len(b)


# making both variable of same length
if alen < blen:
    while alen < blen:
        a = "0" + a
        alen += 1
elif blen < alen:
    while blen < alen:
        b = "0" + b
        blen += 1  
# print(a)
# print(b)

#adding characters from both variables
add,carry = 0,0
ans = ""
for i in range(alen-1, -1,-1):
    add = int(a[i]) + int(b[i]) + carry
    # if carry situation: the following if will deal with it. e.g. add = 3, add//2 = 1(carry), add%2= 1(add)
    if add > 1:
        carry = int(add/2)
        add = add % 2
    else:
        carry = 0
    ans = str(add) + ans

# print(ans)

# if there is any leftover carry
if carry > 0:
#     while carry > 0:
    ans = str(1) + ans
#     carry =-2
print(ans)