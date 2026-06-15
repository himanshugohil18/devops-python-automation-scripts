day_of_week = input("Enter the day of week: ").lower()
print (day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday":
   print ( "i will learn live devops ")
else:
   print ( "i will practice devops ")

num1 = int(input ( "enter your first number: "))
num2 = int(input ( "enter your second number: "))

choise = input ("enter the oprations: (oprations +,-,*,/,%)" )

if choise == "+":
   sum_of_num = num1 + num2
   print ("addition:", sum_of_num)
elif choise == "-":
   diff_of_num = num1 - num2
   print ("subtration:", diff_of_num)
elif choise == "*":
   prod_of_num = num1 * num2
   print ("multiplication:", prod_of_num)
elif choise == "/":
   div_of_num = num1 / num2
   print ("division:", div_of_num)
elif choise == "%":
   mod_of_num = num1 % num2
   print ("modulus:", mod_of_num)
else:
   print ("invalid choise")