def fibonacci_recursive(n):
   
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
      
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def main():
    print("--- Fibonacci Sequence Generator ---")
    try:
    
        terms = int(input("Enter the number of terms (n): "))
        
        if terms <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            print(f"\nFibonacci sequence up to {terms} terms:")
            
            for i in range(terms):
                print(fibonacci_recursive(i), end=" ")
            print()
            
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()