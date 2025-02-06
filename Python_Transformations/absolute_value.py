"""
The issue is that abs() function in Python cannot directly work on lists. You need to use a list comprehension or map to apply abs() 
to each element.

Absolute value means:

 For positive numbers: returns same number
 For negative numbers: returns positive version
 For zero: returns 0

"""

list1 = [4,-9,7,9]

# Using list comprehension
list2 = [abs(x) for x in list1]
# OUTPUT: [4, 9, 7, 9]
list2.sort()
# OUTPUT: [4, 7, 9, 9]


# Alternative using map() function
list2 = list(map(abs, list1))
# OUTPUT: [4, 9, 7, 9]


# Using for loop
list3 = [4,-9,7,-5,-4]
for i in range(len(list3)):
    if list3[i] < 0:
        list3[i] = list3[i] * -1
print(list3)
# OUTPUT: [4, 9, 7, 5, 4]