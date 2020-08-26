class Student:
  count=0   # Class Variable
  #  constructor 
  def __init__(self,name,reg_no,phn_no):
    self.name=name      # instance variable
    self.reg_no=reg_no
    self.phn_no=phn_no

    Student.count = Student.count +1 
    print(f"Welcome {self.name}")

  def printv(self,mark):
    self.mark=mark
    print('Details: ')

    print(self.name)

s1=Student('Mani','18BCS0023','8608687355')
print(s1.__dict__)
s1.printv(90)
print(s1.__dict__)

# Student.printv(s1)

  