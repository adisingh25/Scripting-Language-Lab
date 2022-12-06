from functools import reduce

list1 = []
print('Enter 6 numbers to add to the list :  ')
for i in range (1,7):
    num = int(input())
    list1.append(num)


print(f"The list is : {list1} .")

#creating new list using list-comprehension

list2= [i * 3 for i in list1]
print(f"The new list is : {list2} .")


sum1 = reduce(lambda x,y: x+y,list1)
sum2 = reduce(lambda x,y:x+y,list2)

print("The sum of list1 is : - ", sum1)
print("The sum of list2 is : - ", sum2)