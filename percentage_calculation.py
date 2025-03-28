print("*The numbers must be out of 100")
#taking inputs
math = int(input("Enter the number for maths: "))
science = int(input("Enter the number for science: "))
bangla = int(input("Enter the number for bangla: "))
english = int(input("Enter the number for english: "))
#finding the overall percentage
sum = math + science + bangla + english
perc = (sum/400)*100

print("Percentage: ", perc)