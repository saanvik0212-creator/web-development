num=input("Enter a number:")
n=len(num)
original_num=int(num)
sum_of_powers=0
for digits in num:
    digit=int(digits)
    sum_of_powers += digit ** n
    if sum_of_powers == original_num:
        print(f"{original_num} is an armstrong number.")
    else:
        print(f"{original_num} is not an armstrong number.")