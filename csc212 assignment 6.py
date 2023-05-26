#CSC212 assignment 6
class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+last+'@company.com'
        self.bonus = 0

    def get_pay(self):   #Getting the salary
        return self.pay

    def set_pay(self,pay): #Setter for salary
        self.pay = pay

    def get_bonus(self):    #GEtter for bonus
        return self.bonus

    def set_bonus(self,percent):  #Setter for bonus
        self.bonus = self.pay * percent/100

    def full_name(self):
        return '{} {}'.format(self.first,self.last)

    def __str__(self):
        return 'Employee name: '+self.full_name()+' Employee pay: ' +str(self.pay)+'Employee bonus: '+str(self.bonus)

def read(file):  #This function reads the dirany file
    s = file.read()
    return s

def split_Emp(s):   #this function splits the contents in the dirany file
    s = s.split("/n")
    s=[i.split() for i in s]
    return s

def set_employee(s):   #Creates list and returns it
    emp = []
    bonus = 20
    for i in s:
        e = Employee(i[0],i[1], int(i[2]))
        e.set_bonus(bonus)
        emp.append(e)
        bonus = bonus-1
    return emp

# Reading the dirany file
file = open('dirany.txt', 'r')
s = read(file)
s = split_Emp(s)
emp = set_employee(s)

# COunt the total bonus and number of employees
count = 0
total_bonus = 0.0
for i in emp:
    print(i)
    count += 1
    total_bonus += i.get_bonus()

print("The total number of Employees: ", count)
print("The total bonus paid: ", total_bonus)


