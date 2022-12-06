from functools import reduce


file = open("Part B/2/sample.txt", "r")
# print(file.read())

d = dict()


for line in file:

	line = line.strip()
	line = line.lower()
	words = line.split(" ")
					
  
	for word in words:
	
		if word in d:
		
			d[word] = d[word] + 1
		else:
		
			d[word] = 1




# for key in list(d.keys()):
# 	print(key, ":", d[key])

print(d)
sorted_words = sorted(d.items(), key= lambda x: x[1], reverse=True)
# print(sorted_words)
# newD = dict(sorted_words)     #changing the sorted words into dictionary format
# print(newD)

for i in range(0,10):
    print(sorted_words[i])
    
list2 = []
for i in range(0,10):
    list2.append(len(sorted_words[i][0]))
print(list2)


sum = reduce(lambda x,y: x+y,list2)
print("Avergae length: ",sum/len(list2))


odd = [x**2 for x in range(0,10) if x%2 != 0]
print(odd)


file.close()




