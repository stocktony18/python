print("Tony's Calculator")
selection = input(" + - addition, - - subtraction, * - multiply, / - division:")
firstNumber = int (input ("Num 1: "))
secondNumber = int (input ("Num 2: "))
if(selection == "+"):
 print(firstNumber + secondNumber)
elif(selection == "-"):
 print(firstNumber - secondNumber)
elif(selection == "/"):
 if(secondNumber == 0):
  print("You're wrong")
 else:
  print(firstNumber/secondNumber)
elif(selection == "*"):
 print (firstNumber*secondNumber)
else:
     print("You're Input is wrong sir!")
     

     

    


      


















