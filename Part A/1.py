n = int(input('Enter the number of elements for the list : '))
list1 = []
for _ in range(0,n):
    val = int(input('Enter the value : '))
    list1.append(val)

print(list1)
print('The maximum value from the list is : ', max(list1))
print('The minumum value from the list is : ', min(list1))

newVal = int(input('Enter the new value to added to the list : '))
list1.append(newVal)

delVal = int(input('Enter the value to be deleted : '))
list1.remove(delVal)

print(list1)


findVal = int(input('Enter the value to be searched : '))
if findVal in list1:
    print(findVal, ' is there in the list.')
    print(list1.index(findVal))                #to get the index of the value in the list 
else:
    print(findVal, ' is not there in the list.')


print(list1[::-1])                             #printing the list in the reverse order