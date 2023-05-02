class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def getName(self):
        # print(self.__name)
        return self.__name

    def getAge(self):
        # print(self.__age)
        return self.__age
    
    # def getID(self):
    #     print("Name :", self.__name, "age :", self.__age)

class Employee(Person): 
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.__employeeID = employeeID
    
    def getID(self):
        # super().getID()
        # print(self.getName(), self.getAge(), self.__employeeID)
        print("이름:", self.getName(), " 나이:",self.getAge(), " Id:", self.__employeeID)
        #print("Id :", self.__employeeID)


Employee("IoT", 65, 2018).getID()