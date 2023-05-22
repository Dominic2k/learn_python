#write mode - write to a new file
with open("data2.txt","w") as file:
	file.write("Datpham\n")
	file.write("PhamDucDat")

#write mode - write to a new file
with open("data2.txt","w") as file:
	file.write("a\n")
	file.write("b\n")

#write mode - write to a new file
with open("data2.txt","a") as file:
	file.write("c\n")
	file.write("d\n")
	file.write("e")

with open("data2.txt","r") as file:
	data2 = file.read()
	print(data2)

#Chương trình nhập vào số nguyên n và in ra các số từ n đến 0 trên từng dòng khác nhau
user_input = int(input("Enter an integer: "))

with open("data.txt","w") as file:
	for i in range(user_input):
		file.write(str(user_input - i) + "\n")

numbers = []

with open("data.txt", "r") as file:
	numbers = file.read().split("\n")
	numbers.pop()
#	print(numbers)

for i in range(len(numbers)):
	print("Line 1 " + str(i+1) + ":" + numbers[i])
