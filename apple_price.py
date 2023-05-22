#Chương trình tính tiền của thu ngân khi khách hàng mua và đưa tiền

def calc_total_price(apple_weight, APPLE_PRICE):
	return apple_weight * APPLE_PRICE

def calc_return(total_money_must_pay, money_receive):
	if money_receive < total_money_must_pay:
		return -1
	return money_receive - total_money_must_pay

def print_return_info(total):

	count_500 = int(total/500)
	total = total - 500*count_500
	if count_500 != 0:
		print("500: " + str(count_500))

	count_200 = int(total/200)
	total = total - 200*count_200
	if count_200 != 0:
		print("200: " + str(count_200))

	count_100 = int(total/100)
	total = total - 100*count_100
	if count_100 != 0:
		print("100: " + str(count_100))

	count_50 = int(total/50)
	total = total - 50*count_50
	if count_50 != 0:
		print("50: " + str(count_50))

	count_20 = int(total/20)
	total = total - 20*count_20
	if count_20 != 0:
		print("20: " + str(count_20))

	count_10 = int(total/10)
	total = total - 10*count_10
	if count_10 != 0:
		print("10: " + str(count_10))

	count_1 = int(total)
	if count_1 != 0:
		print("1: " + str(count_1))

def main():
	APPLE_PRICE = 20 #kVND
	apple_weight = input("Enter weight of apples: ")
	money_receive = input("Total money customer give you: ")
	#đổi string thành số thực
	apple_weight = float(apple_weight)
	money_receive = float(money_receive)

	total_money_must_pay = calc_total_price(apple_weight, APPLE_PRICE)
	money_return = calc_return(total_money_must_pay, money_receive)

	print("Total money: " + str(int(total_money_must_pay)))
	if money_return == -1:
		print("Not enough cash")
	else: 
		print("You need to return to customer: " + str(int(money_return)))
		print_return_info(money_return)

main()
