#Tổng hợp kiến thức Python cơ bản
# print("Hello world")
#1.Biến(variables)
#tên biến không bắt đầu bằng số, không được trùng với 1 số keyword của puthon
#tên biến có phân biệt hoa thường
#<tên biến> = <Gía trị của biến>
# a = 10
# b = 15
# s = a + b
# print(s)
#Kiểm tra kiểu dữ liệu của biến
#type(<tên biến>)
#2.Number in python
#Số nguyên intergers
#Kiểu dữ liệu số nguyên là vô hạn trong python
#Số thực trong python có độ chính xác đến 15 chữ số phần thập phân
#Nếu lớn hơn 15 chữ số phải dùng decimal
#b = 9.8838839283776263723627372633463462536427
#type(b)#
#print(type(b))
#Lấy toàn bộ nội dung của thư viện decimal
#from decimal import*
#Lấy tối đa 30 chữ số phần nguyên và phần thập phân decimal
#getcontext().prec = 30
#print(Decimal(10)/Decimal(3))
#Phân số
#from fractions import*
#a = Fraction(4,6)
#print(a)
#print(type(a))
#Số phức
#<phần thực>+<phần ảo>j
a = complex(2,6)
print(a.real)
print(a.imag)
# Dấu // là thương nguyên ( chia lấy phân nguyên )
# Dấu % là chia lấy dư
# --Thư viện math trong python
#import<math>
#math.sqrt(16)
#floor làm tròn xuống
#ceil làm tròn lên