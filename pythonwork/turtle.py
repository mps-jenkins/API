list1 = [-10, -21, -4, 45, -66, 93]

# using list comprehension
sum = 0
neg_nos = [num for num in list1 if num < 0 ]
for num in neg_nos:
    sum = sum + num
print(sum)
