**Best Time Buy and Sell**

- Create two pointers
- Create Max profit holder
- while the right pointer is less than the length of prices - if the prices of the left pointer is less than the right pointer, profit is possible, do not increment the left pointer - else, the left most price is greater than the right most price, so move the left pointer to the right pointer as the right is now the lowest value and could create possbile profit
  -regardless, increment the right pointer as it represents the movement of days

**Binary Search**

- Binary search only works if array is presorted
- We find the target number by going to the middle,
  and seeing if the middle number is the target
- if the middle number is the target, return the middle number
- else if the middle number is less than the target number
- then we cut the left side of the array
- do this by setting the left pointer to the location of th middle + 1
- else the middle number is greater than the target
- we cut off the right side of the array
- We do this by setting the right pointer
  to middle - 1
  we go thru the while loop until the left and right pointer meet/left passes the right pointer ie
  l <= r

**Contains Duplicate**

- Create two dictionaries one for string s, one for string t
- for all the chars in the strings
- make key value pairs and add one to the count of each character
- One dictionaries are made for both strings
- If the counts are disimlar from one array to the next
  return false



**Merge List**
For each list
find if the value of that list1 is <= to the other
if it is <=
set temp.next to list1
list1 = list1.next
temp = list1
if not 
do same for list 2
then check if list 1 and list 2 arent empty and set the tail
to the one that isnt empty
then return dummyHead.next

**Two Sum**
Create a Dictionary
Start the dictionary with 
key: value of target-num[index] : index

then, create a for loop

in this loop
first, find what is needed
do 
needed = target - num[i]

if num[i] is in dictionary
then its match for the target is the index of the key

return dictionary[nums[i]], i

else
  nums[needed] = i
restart looop