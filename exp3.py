#python program to implement abstract datatype

class Student:
    def getstudentdetails(self):
        self.name = input("enter name :")
        self.rollno = int(input("enter rollno :"))
        self.ds = int(input("enter ds marks :"))
        self.maths = int(input("enter maths marks :"))
    def print_res(self):
        self.percentage = (int) ((self.ds + self.maths)/200 * 100)
        print(self.name,self.rollno,self.percentage)



s1=Student()
s1.getstudentdetails()

print("result")
s1.print_res()

s1.ds += 5
s1.maths +=10
print("reault after adding grace marks")
s1.print_res()

