class Employee:
    def __init__(self,name,wage,hiringDate) -> None:
        self._name = name
        self._wage = wage
        self._hiringDate = hiringDate


    def updateWage(self,newAmount):
        self._wage = newAmount

    def __str__(self) -> str:
        return f"Employee name: {self._name} wage: {self._wage} hiring date: {self._hiringDate} "    



class Company: 
    def __init__(self) -> None: 
        self._employees = []

    def addEmployee(self,employee):
        self._employees.append(employee)
    def removeEmployee(self,employee):
        if (self._employees.__contains__(employee)):
            self._employees.remove(employee)
    def showEmployees(self):
        for employee in self._employees:
                print(employee)

e = Employee("jose",1500,"15/05/2021")
e2 = Employee("Andres",2000,"20/02/2019")
c = Company()
c.addEmployee(e)
c.addEmployee(e2)
print("Employees:")
c.showEmployees()
c.removeEmployee(e)
print("Employees after removing: ")
c.showEmployees()