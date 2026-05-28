from user_data import Userdata
from data import Data
from marks import Marks


class Student(Userdata):
    def __init__(self,objname):
        self.dm = Data(objname)
        self.mm = Marks(objname)

        

        self.dm.create_data_file()
        self.student_info = self.dm.data_file_read()

        self.mm.create_marks_file()
        self.student_marks = self.mm.marks_file_read()
        


    def menu(self):
        while True:
            print("""
                    1. Add Student 
                    2. UpDate Info
                    3. Add Marks
                    4. UpDate Marks
                    5. Remove Student
                    6. See All Students
                    7. Exit
                        """)
            try:
                option = int(input("Enter Choice: "))
            except ValueError:
                print("invalid input. ! Enter correct output.")
                continue
            match option:
                case 1:
                    print("Add Student")
                    self.add_stu()
                case 2:
                    print("Update Info")
                    self.upgrade_info()
                case 3:
                    print("Add Marks")
                    self.add_marks()
                case 4:
                    print("Function is not written yet.")
                    continue
                case 5:
                    print("Remove Student")
                    self.remove_stu()
                case 6:
                    print("All Student Data")
                    self.see_stu()
                case 7:
                    print("Good Bye")
                    break
                case _:
                    print("Enter valid input")

    def student_info_getter(self):
        return self.student_info

    def add_stu(self):
        self.stu_data = {
            "Name": super().stu_name(),
            "Roll Number" : super().stu_roll(self.student_info),
            "E-mail": super().stu_email(),
            "Phone Number": super().stu_phone()
        }
        self.student_info.append(self.stu_data)
        self.dm.data_file_write(self.student_info)
        print("Data added Successfully")
    
        

    def see_stu(self):
        print("Student Informaton")
        print(f"| Name | Roll Number | E-mail | Phone Number |")
        for i in self.student_info:
            print(f"| {i.get('Name')} | {i.get('Roll Number')} | {i.get('E-mail')} | {i.get('Phone Number')} |")
    
    def upgrade_info(self):
        roll = int(input("Enter student roll number: "))
        result = super().extract_rollnumber(self.student_info,roll)
        if result == False:
            print("Student not exist.")
        else:
            print("Student Informaton")
            for i in self.student_info:
                if result[1] == i.get('Roll Number'):
                    print(f"Name: {i.get('Name')} | Roll Number: {i.get('Roll Number')} | E-mail: {i.get('E-mail')} | Phone Number: {i.get('Phone Number')}")
                    data = i


            choice = int(input("Enter choice: \n1 for Name \n2 for Email \n3 for Phone Number \n4 for exit \n"))
            match choice:
                case 1:
                    name = super().stu_name()
                    data["Name"] = name
                    self.dm.data_file_write(self.student_info)
                    print("Info Changed")
                case 2:
                    email = super().stu_email()
                    data["E-mail"] = email
                    self.dm.data_file_write(self.student_info)
                    print("Info Changed")
                case 3:
                    phoneNum = super().stu_phone()
                    data["Phone Number"] = phoneNum
                    self.dm.data_file_write(self.student_info)
                    print("Info Changed")
                case 4:
                    print("Nothing to change")
            # self.dm.data_file_write(self.student_info)
            print("Data updated")
    

    def remove_stu(self):
        roll = int(input("Enter student roll number: "))
        result = super().extract_rollnumber(self.student_info,roll)
        if result == False:
            print("Student not exist.")
        else:
            print("Student Informaton")
            for i,d in enumerate(self.student_info):
                if result[1] == d.get('Roll Number'):
                    print(f"Name: {d.get('Name')} | Roll Number: {d.get('Roll Number')} | E-mail: {d.get('E-mail')} | Phone Number: {d.get('Phone Number')}")
                    index = i
            self.student_info.pop(index)
            self.dm.data_file_write(self.student_info)
            print("Student deleted")
    
    
    def add_marks(self):
        roll = int(input("Enter student roll number: "))
        result = super().extract_rollnumber(self.student_info,roll)
        if result == False:
            print("Student not exist.")
        else:
            marklst = input("Enter Marks (space seperated): ")
            self.stu_marks = {
            "Roll Number" : result[1],
            "Marks": marklst.split(" ")
            
        }
        self.student_marks.append(self.stu_marks)
        self.mm.marks_file_write(self.student_marks)
        print("Marks added Successfully")
                    
            

        
        
        
        
objectList = {}

cond = True
while cond:

    objName = input("Enter object name: ").upper()

    if objName in objectList:

        oj = objectList[objName]
        print("Existing object loaded")

    else:

        oj = Student(objName)
        objectList[objName] = oj
        print("New object created")
    
    oj.menu()

    i = input("Enter N to exit: ")
    if i == "n" or i == "N":
        cond = False


   