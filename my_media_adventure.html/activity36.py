def recurfactorial(n):
    if n==1:
        return n
    else:
        return n*recurfactorial(n-1)

num = int(input("Enter a number"))
print(recurfactorial(num))    


def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "num2 cannot be 0"
    return x/y

num1 = int(input("Enter number1"))
num2 = int(input("Enter number2"))

print("Sum:" , add(num1,num2))
print("Difference:" , subtract(num1,num2))
print("Product:" , multiply(num1,num2))
print("Quotient:" , divide(num1,num2))
