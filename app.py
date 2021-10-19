from department import Department
from gender import Gender
from person import Person


p = Person("David", "Harrington", "Mr", Gender.Male)
p.department = Department("Sales", Person("Bill", "Smith", "Mr", Gender.Male))

print("Person: " + p.tostring() + ". Works in " + str(p.department.name))
print("Manager is " + p.department.manager.first_name + " " + p.department.manager.last_name)
print("Fired: " + str(p.fired))

p.fire()

print("Fired: " + str(p.fired))

p.sex_change(Gender.Female, "Doris", "Mrs")

print(p.tostring())
