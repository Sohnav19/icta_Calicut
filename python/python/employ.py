class Employee:
    def __init__(self,a,b,c,d):
        self.code=a
        self.name=b
        self.age=c
        self.salary=d
    def printData(self):
        print("Code : ",self.code)
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Salary : ",self.salary)

e1=Employee(111,"anaga",23,25000)
e1.printData()
e2=Employee(112,"arya",28,35000)
e2.printData()
e3=Employee(113,"veena",45,55000)
e3.printData()
e4=Employee(114,"annu",23,25000)
e4.printData()
e5=Employee(115,"ammu",20,15000)
e5.printData()
