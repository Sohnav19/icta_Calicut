class Students:
    def __init__(self,a,b):
        self.name=a
        self.rollno=b

    def printData(self):
        print("Name =  ",self.name)
        print("RollNo = ",self.rollno)

    def getAge(self,myAge):
        print("Age is ",myAge)

s=Students("Rahul R",1)

x=int(input("enter the age : "))

s.printData()
s.getAge(x)






