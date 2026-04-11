import numpy as np
print(np.__version__)

def calculator():
    print("\n--- NumPy Smart Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter choice (1-4): "))

    # Take input as list → convert to NumPy array
    arr1 = np.array(list(map(float, input("Enter first numbers (space-separated): ").split())))
    arr2 = np.array(list(map(float, input("Enter second numbers (space-separated): ").split())))

    if choice == 1:
        result = np.add(arr1, arr2)
    elif choice == 2:
        result = np.subtract(arr1, arr2)
    elif choice == 3:
        result = np.multiply(arr1, arr2)
    elif choice == 4:
        result = np.divide(arr1, arr2)
    else:
        print("Invalid choice")
        return

    print("Result:", result)


# Run
while True:
    calculator()
    cont = input("Continue? (y/n): ")
    if cont.lower() != 'y':
        break