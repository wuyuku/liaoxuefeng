'''
sum = 0
# ()是tuple,不可变；[]是list,可变
for x in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    sum = sum + x
print (sum)
'''

#print (list(range(101)))

sum = 0
for x in range(101):
    sum = sum + x
print (sum)