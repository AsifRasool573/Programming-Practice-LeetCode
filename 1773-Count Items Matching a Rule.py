1773. Count Items Matching a Rule

You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei. ruleKey == "color" and ruleValue == colori. ruleKey == "name" and ruleValue == namei. Return the number of items that match the given rule.


Example 1:
Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],
ruleKey = "type", ruleValue = "phone"

Output: 2

Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"].
Note that the item ["computer","silver","phone"] does not match.




#First Logic (Working)

items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"

count = 0

#firstly we'll make the index according to given instructions

if ruleKey == "type":
  index = 0

elif ruleKey == "color":
  index = 1

else:
  index = 2

# traverse the list
for item in items:
  if ruleValue == item[index]:
    count += 1

print(count)


=============================================================

#2nd Logic (Working)


items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"

count = 0

for i in range(len(items)):
  if ruleKey == "type" and ruleValue == items[i][0]:
    count += 1

  elif ruleKey == "color" and ruleValue == items[i][1]:
    count += 1

  elif ruleKey == "name" and ruleValue == items[i][2]:
    count += 1


print(count)
