# from base import Student1

class Userdata:
    
    rollNumCounter = 1

    

    def stu_name(self):

        name = input("Enter your Name: ")
        
        if len(name) > 3 and len(name) < 50 and name.isalpha():
            return name
        else:
            if len(name) < 3 or len(name) > 50:
                print("lenght should be greater than 3 and less 50 chars")
            else:
                print("Only Alphabets are allowed")
        return self.stu_name()

    def stu_roll(self, student_info):
        if not student_info:
            return 1
        existing_rolls = [i.get('Roll Number') for i in student_info if i.get('Roll Number')]
        return max(existing_rolls) + 1
    
    def stu_email(self):
        email = input("Enter Student Email: ")
        if email.endswith("@gmail.com") and len(email) < 50:
            return email
        else:
            print("Email must ends with '@gmail.com' . ")
            return self.stu_email()
        
    def stu_phone(self):
        phone = input("Enter Phone Number: ")
        if phone.isdecimal() and len(phone) == 11:
            return phone
        else:
            if len(phone) != 11:
                print("Phone number must have 11 digits.")
            else:
                print("Numbers are Allowed Only")
            return self.stu_phone()

    
    def extract_rollnumber(self,a:list,b:int):
        rollNumbers = []
        for i in a:
            rollNumbers.append(i.get('Roll Number'))
        
        if b in rollNumbers:
            return (True, b)
        else:
            return False
            

   








