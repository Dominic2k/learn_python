
# colors.append("yellow")
# #thêm append là vào vị trí cuối

# for i in range(len(colors)):
# 	print(colors[i])

# last_index = len(colors)-1

# print(colors[-1])
colors = ["red", "blue", "green", "gray", "red", "red"]
print(colors)

# remove from list
try:
	colors.remove("blue")
except:
	print("Not exist")
print(colors)

 #bỏ đi cái cuối cùng (remove last element)
colors.pop()
print(colors)

#Thêm 1 element vào vị trí thứ ...
colors.insert(0,"black")
print(colors)
colors.insert(1,"purple")
print(colors)

#tìm vị trí thứ ? của 1 element (red)
print(colors.index("red"))

#tìm tất cả các vị trí của 1 element (red)
red_index = []
for i in range(len(colors)):
	if colors[i] == "red":
		red_index.append(i)
print("The word 'red' occurs at the following index: ", end = " ")
print(red_index)

#find number of occurance of "red"
# đếm số phần tử tên red trong list
print(colors.count("red"))

#Sắp xếp
print("Sort Example: ")
a = [1,2,10,3,5,7]
a.sort()
print(a)

#change the first element to 'Dat'
a[0] = "Dat"
print(a)

