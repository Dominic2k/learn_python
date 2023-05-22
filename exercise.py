#Bài tập tính tổng S
s_denominator = 0 # khai báo phần mẫu số

for i in range(100):
	if i == 1: # loại bỏ số 1
		continue

	if i % 2 == 0: #loại bỏ số chẵn
		continue

	s_denominator += 1/i # tổng của mẫu số

s = 1/s_denominator # tổng cuối
s = round(s,2) #làm tròn 2 chữ số
print("S = " + str(s))

#
#Dùng vòng while lặp để in ra chuỗi các số
i = -2
while i<6:
	i += 2
	if i == 5:
		continue
	print(i)
#in ra 0246
i = -1
while i<8:
	i += 2
	if i == 5:
		continue
	print(i)
#in ra 1379