
class Employee:
    company = "abc" # class attribute
    salary = 120000

    # NOTE this is wrong
    # def getInfo():
    #     print(f"The company name is {company} and salary is {salary}")

    # NOTE this by default takes the insatnce of the class as argument --- you have to provide self as argument in every function
    def getInfo(self):
        print(f"The company name is {self.company} and salary is {self.salary}")
        


Fatima = Employee()
# Fatima.getInfo() this is wrong it will give an error because this is get converted inot Employee.getinfo(Fatima) we have to pass the instance


# They both are same
Fatima.getInfo() 
# OR 
Employee.getInfo(Fatima)

