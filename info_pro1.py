	#Chương trình nhập vào và in ra thông tin
import datetime

def ask_yes_no(prompt):
	while True:
		answer = input(prompt)
		if(answer == "yes"):
			return True
		elif answer == "no":
			return False
		else:
			continue
def calculate_age(year_born):
	now = datetime.datetime.now()
	CURRENT_YEAR = now.year
	return CURRENT_YEAR - year_born

def convert_meter_to_feet(meter):
	METER_TO_FEET = 3.281
	feet = meter * METER_TO_FEET
	feet = round(feet,1)
	return feet

def print_height_info(feet, is_male):
	if is_male == True: #Nam
		if feet > 6.5:
			print("You are", end=" ")
			
			#using for loop to print very 10 time
			for i in range (10):
				print("very", end=" ")

			print("tall as a man")
		elif feet > 6.0:
			print("You are tall as a man")
		else:
			print("You are short as a man")
	else:
		if feet > 5.7:
			print("You are tall as a girl")
		elif feet < 5.0:
			print("You are", end=" ")

			#using while loop to print very 10 time
			i = 0
			while i<10:
				print("very", end=" ")
				i+=1

			print("short as a girl")
		else:
			print("You are short as a girl")

def print_person_info(firstname, lastname, age, feet, is_vietnam, is_male):
	now = datetime.datetime.now()
	CURRENT_YEAR = now.year
	print("-----Info-----\n")
	print("Your name is " + firstname + " " + lastname)
	print("You are {0} years old in {1}".format(age,CURRENT_YEAR))
	print(("You are ") + str(feet) + " feet tall.")
	if is_vietnam == True:
		print("Xin chao")
	else:
		print("Welcome")
	print_height_info(feet, is_male)

def ask_person_info():
	firstname = input("Your first name: ")
	lastname = input("Your last name: ")
	year_born = int(input("When you were born ? "))
	height_meter = float(input("Your height (meter): "))
	is_male = ask_yes_no("Are you male: (yes/no) ")
	is_vietnam = ask_yes_no("Are you Vietnam? ")
	return firstname, lastname, year_born, height_meter, is_male, is_vietnam

def main():
	firstname, lastname, year_born, height_meter, is_male, is_vietnam = ask_person_info()
	age = calculate_age(year_born)
	feet = convert_meter_to_feet(height_meter)
	print_person_info(firstname, lastname, age, feet, is_vietnam, is_male)

main()


# #Chương trình nhập vào và in ra thông tin
# CURRENT_YEAR = 2023
# METER_TO_FEET = 3.281

# firstname = input("Your first name: ")
# lastname = input("Your last name: ")
# year_born = input("When you were born ? ")
# height_meter = input("Your height (meter): ")

# list_answer = ["y","n","Yes","No","yes","no"]
# while True:
# 	gender_input = input("You are male ?(yes/no):")
# 	if gender_input in list_answer:
# 		break

# year_born = int(year_born)
# age = CURRENT_YEAR - int(year_born)

# height_meter = float(height_meter)
# height_feet = height_meter * METER_TO_FEET
# height_feet = round(height_feet,1)

# print("-----Info-----\n")
# print("Your name is " + firstname + " " + lastname)
# print("You are {0} years old in {1}".format(age,CURRENT_YEAR))
# #print("You are " + str(age) + " years old in " + str(CURRENT_YEAR))
# #Dùng format để thay cho đoạn trên
# print(("You are ") + str(height_feet) + " feet tall.")

# is_male = None

# if (gender_input =="yes") or (gender_input == "y") or (gender_input == "Yes"):
# 	is_male = True
# else:
# 	is_male = False

# if is_male == True: #Nam
# 	if height_feet > 6.5:
# 		print("You are", end=" ")
		
# 		#using for loop to print very 10 time
# 		for i in range (10):
# 			print("very", end=" ")

# 		print("tall as a man")
# 	elif height_feet > 6.0:
# 		print("You are tall as a man")
# 	else:
# 		print("You are short as a man")
# else:
# 	if height_feet > 5.7:
# 		print("You are tall as a girl")
# 	elif height_feet < 5.0:
# 		print("You are", end=" ")

# 		#using while loop to print very 10 time
# 		i = 0
# 		while i<10:
# 			print("very", end=" ")
# 			i+=1

# 		print("short as a girl")
# 	else:
# 		print("You are short as a girl")

