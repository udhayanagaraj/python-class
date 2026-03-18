class Student:
    def __init__(self,first_Name,last_Name,age,address,mobile):
        self.first_Name=first_Name
        self.last_Name=last_Name
        self.age=age
        self.address=address
        self.mobile=mobile
        try:
            self.validate()
        except ValueError as e: 
            print("Exception: ",e)
            
    def __str__(self):        
       return f"first_Name='{self.first_Name}', last_Name='{self.last_Name}', age={self.age}, address='{self.address}', mobile={self.mobile}"
    
    def update_details(self,first_Name,last_Name,age,address,mobile):
        if (first_Name == last_Name or (age>18 and age<60) or len(str(mobile)) !=10 or address ==" "  or not mobile.startswith("9")):
            raise ValueError("Invalid input")
            
        else:
            self.first_Name=first_Name
            self.last_Name=last_Name
            self.age=age
            self.address=address
            self.mobile=mobile

    def print_test(self):
        print("hello")
        
    def validate(self):
        if self.first_Name == self.last_Name or (self.age<18 and self.age>60) or len(str(self.mobile)) != 10 or self.address == "" or not self.mobile.startswith("9"):
            raise ValueError("Invalid input")



students = []

def call_data():
    student1 = Student("Udhaya","Nagaraj",25,"chennai","9876543210")
    student2 = Student("Vidhya","Sasikumar",19,"chennai","9876543210")
    student3 = Student("Hari","Lakshaman",30,"madurai","9765432109")
    student4 = Student("Kumar","Lakshmana",35,"salem","9654321098")

    students.append(student1)
    students.append(student2)
    students.append(student3)
    students.append(student4)

data = "yes"
while data != "no":
    call_data()
    for student in students:
        print(student)
    students.clear()
    data = input("Do you want to continue?")



