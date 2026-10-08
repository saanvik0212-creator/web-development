import datetime
import calendar
now = datetime.datetime.now()
print("Time now is:",now)
print(calendar.calendar(2053))

temp=float(input("Enter temperature"))
if temp>10:
  print("The temperature quite low!")
elif temp>25 and temp<=35:
  print("Grab your jacket and get ready")
elif temp>35 and temp<=45:
  print("Nice weather to go out")
elif temp>45 and temp<=50:
  print("it's really burning hot out there!")
else:
  print("Good atmosphere")


  num =0
while num<18:
  print(num)
  num=num+1

  num1=int(input("Enter a number"))
isPrime=True
for i in range(2,num1):
   if(num1%i==0):
    isPrime=False
    print("Not a prime number")
    break
if(isPrime==True):
 print("Is a prime number")