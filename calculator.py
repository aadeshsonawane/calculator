
def operation(proc,x,y):
  if proc == "+":
     print(x + y)
     print("Thank you for using :)")
  elif proc == "-":
     print(x - y)
     print("Thank you for using :)")
  elif proc == "*":
     print(x * y)
     print("Thank you for using :)")
  elif proc == "/":
     print(x / y)
     print("Thank you for using :)")
  else :
     print("invalid operation")



x = int(input("Enter first no. "))
proc =(input("Enter operation(+, -, *, / )"))
y = int(input("Enter secound no. "))

operation(proc,x,y)
