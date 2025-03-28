#taking input
Amount = int(input("Please Enter Amount for Wthdraw: "))

#calculating the amount of notes of different denominations
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10
#printing the values
print("100 tk notes: ", note_1)
print("50 tk notes: ", note_2)
print("10 tk notes: ", note_3)