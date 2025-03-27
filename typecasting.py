#making the variables
name = "Suhana"
age = 13
weight = 43.5
is_student = True

#printing different variables and their Data Type
print("Name: ", name)
print("Data-Type of name is: ", type(name))

print("Age: ", age)
print("Data-Type of age is:", type(age))

print("Weight: ", weight)
print("Data-Type of weight is: ", type(weight))

print("Is_student: ", is_student)
print("Data-Type of is_student: ", type(is_student))

#Type casting to convert the data type of the variables
print("\n After Type Casting")
age = str(age)
print("Data Type of age: ", type(age))

weight = int(weight)
print("Data Type of weight: ", type(weight))

is_student = str(is_student)
print("Data Type of is_student: ", type(is_student))