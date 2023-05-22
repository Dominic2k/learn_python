#Tạo  class chứa thông tin của học sinh sau đó có thể thêm học sinh vào và gọi ra.
class Student:
	def __init__(self, name, age, math_score, literature_score):
		self.name = name
		self.age = age
		self.math_score = math_score
		self.literature_score = literature_score
		self.teacher = "DungLai"

	def average_score(self):
		ave_score = (self.math_score + self.literature_score)/2
		return ave_score

	def print_info(self):
		ave = str(self.average_score()) #gọi hàm trong hàm của 1 class
		print("Student name: "  + self.name + " " + str(self.age) + " years old " + " study with " + self.teacher + " have average score: " + ave)

#create
students = []
s1 = Student("Man", 21, 6, 8)
s2 = Student("Women", 22, 8, 9)
s3 = Student("Kid", 23, 4, 7)
#insert
s2.teacher = "Jean"
#add three student 1 2 3 into list student
students.append(s1)
students.append(s2)
students.append(s3)

for i in range(len(students)):
	students[i].print_info()
